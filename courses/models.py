from django.db import models
import uuid

# Create your models here.
class Base(models.Model):
  id = models.UUIDField(primary_key=True, editable=False,default=uuid.uuid4)
  created_at = models.DateTimeField(auto_now_add=True) 
  updated_at = models.DateTimeField(auto_now=True)
  active = models.BooleanField(default=True)
  
  class Meta:
    abstract = True
  
class Course(Base):
  title = models.CharField(max_length=255)
  description = models.TextField()
  url = models.URLField()
  
  class Meta:
    verbose_name = 'Course'
    verbose_name_plural = 'Courses'
    
    def __str__(self):
      return self.title
  
class Evaluation(Base):
  name = models.CharField(max_length=255)
  course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='evaluations')
  rating = models.DecimalField(max_digits=2, decimal_places=1)
  email = models.EmailField()
  comment = models.TextField(max_length=500, blank=True, null=True, default=None)
  
  class Meta:
    verbose_name = 'Evaluation'
    verbose_name_plural = 'Evaluations'
    unique_together = ('email', 'course')
    
    def __str__(self):
      return f'Evaluator:{self.name} \n Course:{self.course.title} \n Rating:{self.rating}'