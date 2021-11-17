from django.db import models


class Student(models.Model):
    rn = models.IntegerField()
    fname = models.CharField(max_length=40)
    lname = models.CharField(max_length=40)
    dob = models.DateField()
    email = models.EmailField()
    addr = models.TextField()
