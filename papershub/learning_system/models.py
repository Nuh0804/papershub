from django.db import models
from uuid import uuid4
from django.core.validators import FileExtensionValidator
from django.conf import settings

# Create your models here.
class DegreeProgram(models.Model):
    id = models.CharField(max_length=255, unique=True, primary_key=True)
    degree_name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f'{self.id}'
    
    

class Course(models.Model):
    id = models.CharField(primary_key = True, max_length = 255)
    name = models.CharField( max_length = 255)
    degree_id = models.ForeignKey(DegreeProgram, on_delete=models.CASCADE)
    description = models.TextField()
    year_taught = models.IntegerField(choices=((1, 'Year 1'), (2, 'Year 2'), (3, 'Year 3'), (4, 'Year 4')))

    def __str__(self) -> str:
        return f'{self.id}'
    

class Lecture(models.Model):
    id = models.UUIDField(primary_key = True, default= uuid4, editable = False, 
        unique=True)
    course_id = models.ForeignKey(Course, on_delete = models.CASCADE)
    title = models.CharField(max_length = 255)
    file = models.FileField(upload_to='lecture_notes/', validators=[FileExtensionValidator(allowed_extensions=['pdf', 'png'])])

    def __str__(self) -> str:
        return f'{self.title}'

class Tutorial(models.Model):
    id = models.UUIDField(primary_key = True, default= uuid4, editable = False, 
        unique=True)
    course_id = models.ForeignKey(Course, on_delete = models.CASCADE)
    title = models.CharField(max_length = 255)
    file = models.FileField( upload_to='tutorials/', validators=[FileExtensionValidator(allowed_extensions=['pdf', 'png'])])

    def __str__(self) -> str:
        return f'{self.title}'

class PastPaper(models.Model):
    id = models.UUIDField(primary_key = True, default= uuid4, editable = False, 
        unique=True)
    course_id = models.ForeignKey(Course, on_delete = models.CASCADE)
    title = models.CharField(max_length = 255)
    file = models.FileField(upload_to='past papers/', validators=[FileExtensionValidator(allowed_extensions=['pdf', 'png'])])
    solution = models.FileField(blank=True, upload_to='solutions/', validators=[FileExtensionValidator(allowed_extensions=['pdf', 'png'])])

    def __str__(self) -> str:
        return f'{self.title}'