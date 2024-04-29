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
    
class Year(models.Model):
    id = models.IntegerField(primary_key=True)

    def __str__(self) -> str:
        return f'{self.id}'

class Semester(models.Model):
    id = models.IntegerField(primary_key=True)

    def __str__(self) -> str:
        return f"{self.id}"

class Course(models.Model):
    id = models.CharField(primary_key = True, max_length = 255)
    name = models.CharField( max_length = 255)
    degree_id = models.ManyToManyField(DegreeProgram)
    description = models.TextField()
    year_taught = models.ManyToManyField(Year)
    semester = models.ManyToManyField(Semester)
    notes = models.TextField(max_length=255)

    def __str__(self) -> str:
        return f'{self.id}'
    


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