from django.contrib import admin
from .models import Course, Evaluation
# Register your models here.

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'active', 'url', 'updated_at')
    search_fields = ('title', 'description')

@admin.register(Evaluation)
class EvaluationAdmin(admin.ModelAdmin):
    list_display = ('name', 'course', 'rating')
    search_fields = ('name', 'course__title')