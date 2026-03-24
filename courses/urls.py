from django.urls import path
from .views import CourseAPIView, CoursesAPIView, EvaluationAPIView, EvaluationsAPIView, EvaluationViewSet, CourseViewSet
from rest_framework.routers import SimpleRouter


router = SimpleRouter()
router.register('courses', CourseViewSet)
router.register('valuations', EvaluationViewSet)

urlpatterns = [
  path('courses/',CoursesAPIView.as_view(), name='Courses'),
  path('courses/<int:course_pk>/',CourseAPIView.as_view(), name='Course'),
  path('courses/<int:course_pk>/evaluations/',EvaluationsAPIView.as_view(), name='Course Evaluations'),
  path('evaluations/',EvaluationsAPIView.as_view(), name='Evaluations'),
  path('evaluations/<int:evaluation_pk>/',EvaluationAPIView.as_view(), name='Evaluation')
]