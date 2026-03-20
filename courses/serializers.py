from rest_framework import serializers
from .models import Course, Evaluation


class EvaluationSerializer(serializers.ModelSerializer):
	class Meta:
		model = Evaluation
		extra_kwargs = {
				'email': {'write_only': True}
		}
		fields = (
				'id',
				'name',
				'email',
				'comment',
				'rating',
				'course',
		)
class CourseSerializer(serializers.ModelSerializer):
	class Meta:
		model = Course
		fields = (
			'id',
			'title',
			'description',
			'active',
			'url',
			'updated_at',
		)
