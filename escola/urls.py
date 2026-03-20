
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('api/v1/', include('courses.urls')),
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework.urls')),
]
