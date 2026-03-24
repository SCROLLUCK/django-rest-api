from django.urls import path
from .views import CourseAPIView, CoursesAPIView, EvaluationAPIView, EvaluationsAPIView, EvaluationViewSet, CourseViewSet
from rest_framework.routers import SimpleRouter
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView


# V1 Urls
urlpatterns = [
  path('courses/',CoursesAPIView.as_view(), name='Courses'),
  path('courses/<str:pk>/',CourseAPIView.as_view(), name='Course'),
  path('courses/<str:pk>/evaluations/',EvaluationsAPIView.as_view(), name='Course Evaluations'),
  path('evaluations/',EvaluationsAPIView.as_view(), name='Evaluations'),
  path('evaluations/<str:pk>/',EvaluationAPIView.as_view(), name='Evaluation'),
  
  path('schema/', SpectacularAPIView.as_view(), name='schema'),
  path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
  path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc')
]

# V2 Router
router = SimpleRouter()
router.register('courses', CourseViewSet)
router.register('valuations', EvaluationViewSet)

