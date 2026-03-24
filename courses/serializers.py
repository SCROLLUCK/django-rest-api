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
  
  #. 1 - Nested Relationship
	evaluations = EvaluationSerializer(many=True, read_only=True)	
  
	#. 2 - Hyperlinked Related Field
	# evaluations = serializers.HyperlinkedRelatedField(
	# 	many=True,
	# 	read_only=True,
	# )
	
	#. 3 - Primary Key Related Field		
	# evaluations = serializers.PrimaryKeyRelatedField(
	# 	many=True,
	# 	read_only=True
	# )	
	
	class Meta:
		model = Course
		fields = (
			'id',
			'title',
			'description',
			'active',
			'url',
			'evaluations',
			'updated_at',
		)
  
		course = serializers.SlugRelatedField(
			read_only=True,
			slug_field='title',
   )
