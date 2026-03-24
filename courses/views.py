from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Course, Evaluation
from .serializers import CourseSerializer, EvaluationSerializer

# ================= API V1 =================
class CoursesAPIView(generics.ListCreateAPIView):
		queryset = Course.objects.all()
		serializer_class = CourseSerializer
 
class CourseAPIView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Course.objects.all()
	serializer_class = CourseSerializer

class EvaluationsAPIView(generics.ListCreateAPIView):
		queryset = Evaluation.objects.all()
		serializer_class = EvaluationSerializer

		def get_queryset(self):
				course_pk = self.kwargs.get('course_pk')
				if course_pk:
						return self.queryset.filter(course_id=course_pk)
				return self.queryset.all()
 
class EvaluationAPIView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Evaluation.objects.all()
	serializer_class = EvaluationSerializer

# ================= API V2 =================

class CourseViewSet(viewsets.ModelViewSet):
		queryset = Course.objects.all()
		serializer_class = CourseSerializer
  
		@action(detail=True, methods=['get'])
		def evaluations(self, request, pk=None):
				course = self.get_object()
				evaluations = course.evaluations.all()
				serializer = EvaluationSerializer(evaluations, many=True)
				return Response(serializer.data)
  
class EvaluationViewSet(viewsets.ModelViewSet):
		queryset = Evaluation.objects.all()
		serializer_class = EvaluationSerializer
  
''' VIEWSET COM MIXINS
class EvaluationViewSet(mixins.ListModelMixin,
						mixins.CreateModelMixin,
						mixins.RetrieveModelMixin,
						mixins.UpdateModelMixin,):
		queryset = Evaluation.objects.all()
		serializer_class = EvaluationSerializer
'''