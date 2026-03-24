from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Course, Evaluation
from .serializers import CourseSerializer, EvaluationSerializer

class CourseAPIView(APIView):
	def get(self, request):
		courses = Course.objects.all()
		serializer = CourseSerializer(courses, many=True)
		return Response(serializer.data)

	def post(self, request):
		serializer = CourseSerializer(data=request.data)
		if serializer.is_valid(raise_exception=True):
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EvaluationAPIView(APIView):
	def get(self, request):
		evaluations = Evaluation.objects.all()
		serializer = EvaluationSerializer(evaluations, many=True)
		return Response(serializer.data)

	def post(self, request):
		serializer = EvaluationSerializer(data=request.data)
		if serializer.is_valid(raise_exception=True):
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)