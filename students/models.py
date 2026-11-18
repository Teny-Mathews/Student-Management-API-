from django.db import models


class Student(models.Model):
    name=models.CharField(max_length=20)
    roll_number=models.IntegerField()
    course=models.CharField(max_length=20)
    age=models.IntegerField()
    place=models.CharField(max_length=20)
    image=models.ImageField(upload_to="students",null=True)
