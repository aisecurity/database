from django.db import models

# Create your models here.
class StudentLog(models.Model):
    student_id = models.IntegerField()
    name = models.CharField(max_length=50)
    time = models.DateTimeField()

class UnknownLog(models.Model):
    time = models.DateTimeField()
    path_to_img = models.CharField(max_length=10000)
    #path_to_img = FilePathField()