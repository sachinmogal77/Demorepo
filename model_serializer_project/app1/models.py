from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=30)
    marks = models.FloatField()
    course=models.CharField(max_length=20)
    city = models.CharField(max_length=30)
    qualification=models.CharField(max_length=30)

