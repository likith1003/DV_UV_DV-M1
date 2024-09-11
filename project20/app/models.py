from django.db import models

# Create your models here.
class School(models.Model):
    sname = models.CharField(max_length=50)
    princy = models.CharField(max_length=50)
    loc = models.CharField(max_length=50)

    def __str__(self):
        return self.sname
    

class Student(models.Model):
    sname = models.ForeignKey(School, on_delete=models.CASCADE, related_name='schools')
    stdname = models.CharField(max_length=50)
    stdclass = models.IntegerField()
    stdadd = models.CharField(max_length=50)