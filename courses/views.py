from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from .models import Course, Evaluation
from .serializers import CourseSerializer, EvaluationSerializer

class CoursesAPIView(generics.ListCreateAPIView):
	queryset = Course.objects.all()
	serializer_class = CourseSerializer
 
class CourseAPIView(generics.RetrieveUpdateDestroyAPIView):
  queryset = Course.objects.all()
  serializer_class = CourseSerializer

class EvaluationsAPIView(generics.ListCreateAPIView):
	queryset = Evaluation.objects.all()
	serializer_class = EvaluationSerializer
 
class EvaluationAPIView(generics.RetrieveUpdateDestroyAPIView):
  queryset = Evaluation.objects.all()
  serializer_class = EvaluationSerializer
