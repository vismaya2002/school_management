from django.db import models

# Create your models here.

class StudentDetails(models.Model):
    student_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    grade = models.IntegerField()
    section = models.CharField(max_length=5)
    rollnumber = models.IntegerField()


