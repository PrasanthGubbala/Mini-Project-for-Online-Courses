from time import timezone

from django.db import models
from datetime import datetime


class Admin(models.Model):
    name = models.CharField(max_length=30)
    user_name = models.CharField(max_length=30,unique=True,primary_key=True)
    contact = models.IntegerField(unique=True)
    city = models.CharField(max_length=30)
    password = models.CharField(max_length=20)

class CourseInfo(models.Model):
    course_id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=30,unique=True)
    tutor = models.CharField(max_length=30)
    start_date = models.DateField(default=datetime.now())
    class_time = models.TimeField(default=12-00)
    fee = models.IntegerField(default=3000)
    duration = models.IntegerField(default=45)


class StudentInfo(models.Model):
    name = models.CharField(max_length=30)
    contact = models.IntegerField(unique=True)
    email = models.EmailField(primary_key=True,unique=True)
    password = models.CharField(max_length=20)

class EnrolledCourses(models.Model):
    email = models.EmailField()
    course_id = models.IntegerField(unique=True)