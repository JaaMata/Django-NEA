from string import ascii_lowercase
from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import SET_NULL
from random import choice
# Create your models here.


class Teacher(models.Model):
    account = models.ForeignKey(User, on_delete=SET_NULL, null=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class TutorGroup(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=SET_NULL, null=True)
    tutor_code = models.CharField(max_length=7)

    def __str__(self):
        return self.tutor_code


class Student(models.Model):
    gender_choices = (('Male', 'Male'), ('Female', 'Female'))

    student_id = models.CharField(max_length=13, unique=True, primary_key=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    home_address = models.CharField(max_length=200)
    home_phone_number = models.CharField(max_length=11)
    gender = models.CharField(max_length=20, choices=gender_choices)
    tutor_group = models.ForeignKey(TutorGroup, on_delete=SET_NULL, null=True)
    email = models.EmailField()

    def email_gen(obj):
        email = obj.last_name.lower()[:3] + obj.first_name.lower()[:3] + \
            '@treeroadschool.derbyshire.sch.uk'
        return email

    def generate_id():
        id = ""
        for i in range(13):
            id += choice(ascii_lowercase)
        return id

    def __str__(self) -> str:
        return self.first_name + ' ' + self.last_name
