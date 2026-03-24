from django.urls import path
from .views import CourseAPIView, CoursesAPIView,EvaluationAPIView, EvaluationsAPIView

urlpatterns = [
  path('courses/',CoursesAPIView.as_view(), name='Courses'),
  path('courses/<int:pk>/',CourseAPIView.as_view(), name='Course'),
  path('evaluations/',EvaluationsAPIView.as_view(), name='Evaluations'),
  path('evaluations/<int:pk>/',EvaluationAPIView.as_view(), name='Evaluation')
]