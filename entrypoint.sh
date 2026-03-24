#!/bin/bash
# entrypoint.sh

set -e

echo "🚀 Iniciando entrypoint..."

# Aguardar PostgreSQL
echo "⏳ Aguardando PostgreSQL..."
until PGPASSWORD=$DB_PASSWORD psql -h "$DB_HOST" -U "$DB_USER" -d "$DB_NAME" -c '\q' 2>/dev/null; do
  echo "📡 PostgreSQL indisponível - aguardando..."
  sleep 2
done
echo "✅ PostgreSQL disponível!"

# Criar diretórios necessários
echo "📁 Criando diretórios..."
mkdir -p /app/staticfiles
mkdir -p /app/static
mkdir -p /app/media

# Verificar se as migrações existem
echo "📦 Verificando migrações..."
python manage.py makemigrations --noinput

# Aplicar migrações
echo "🗄️  Aplicando migrações..."
python manage.py migrate --noinput

# Criar superusuário automaticamente
echo "👤 Verificando superusuário..."
python manage.py shell << END
from django.contrib.auth import get_user_model
from django.db import connection

User = get_user_model()
if connection.introspection.table_names():
    if not User.objects.filter(is_superuser=True).exists():
        username = '${DJANGO_SUPERUSER_USERNAME:-admin}'
        email = '${DJANGO_SUPERUSER_EMAIL:-admin@example.com}'
        password = '${DJANGO_SUPERUSER_PASSWORD:-admin123}'
        
        User.objects.create_superuser(username, email, password)
        print(f"✅ Superusuário criado ({username}/{password})")
    else:
        print("✅ Superusuário já existe")
else:
    print("⚠️  Tabelas ainda não criadas")
END

# Coletar arquivos estáticos (com flag para não interagir)
echo "📁 Coletando arquivos estáticos..."
python manage.py collectstatic --noinput --clear

# Executar o comando recebido
echo "🎯 Executando comando: $@"
exec "$@"