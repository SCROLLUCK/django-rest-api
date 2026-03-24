# Makefile
.PHONY: help build up down logs migrate shell psql

help:
	@echo "Comandos disponíveis:"
	@echo "  make build    - Construir as imagens"
	@echo "  make up       - Iniciar os containers"
	@echo "  make down     - Parar os containers"
	@echo "  make restart  - Reiniciar os containers"
	@echo "  make logs     - Ver logs"
	@echo "  make migrate  - Executar migrações"
	@echo "  make shell    - Acessar shell do Django"
	@echo "  make psql     - Acessar PostgreSQL"
	@echo "  make clean    - Limpar tudo (containers, volumes)"

build:
	docker compose build --no-cache

up:
	docker compose up -d
	@echo "✅ Containers iniciados!"
	@echo "🌐 Acesse: http://localhost:8000"

down:
	docker compose down

restart: down up

logs:
	docker compose logs -f

migrate:
	docker compose exec web python manage.py makemigrations
	docker compose exec web python manage.py migrate

shell:
	docker compose exec web python manage.py shell

psql:
	docker compose exec db psql -U ${POSTGRES_USER} -d ${POSTGRES_DB}

clean:
	docker compose down -v
	docker system prune -f
	@echo "✅ Ambiente limpo!"

status:
	docker compose ps
	@echo "\n📊 Status do banco:"
	docker compose exec db pg_isready -U ${POSTGRES_USER}