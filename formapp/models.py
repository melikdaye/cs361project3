__author__ = 'admin'

from django.db import models

# Create your models here.



class teachers(models.Model):
    first_name=models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    office_details = models.TextField()
    phone = models.IntegerField()
    email = models.EmailField()

    def __unicode__(self):
        return self.first_name +' '+ self.last_name

class students(models.Model):
    first_name=models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    course = models.ManyToManyField('courses')

    def __unicode__(self):
        return self.first_name +' '+ self.last_name

class courses(models.Model):
    course_name=models.CharField(max_length=50)
    code=models.CharField(max_length=30)
    classroom=models.CharField(max_length=30)
    time=models.TimeField()
    teacher=models.ForeignKey(teachers)
    def __unicode__(self):
        return  self.code +' '+self.course_name

