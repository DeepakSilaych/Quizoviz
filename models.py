from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class question(models.Model):
    question_id = models.CharField(max_length=10)
    question_test= models.CharField(max_length=500)
    option_a = models.CharField(max_length=500)
    option_b = models.CharField(max_length=500)
    option_c = models.CharField(max_length=500)
    option_d = models.CharField(max_length=500)
    correct_option = models.CharField(max_length=1)


class teacher(models.Model):
    teacher_id = models.CharField(max_length=10)
    teacher_name = models.CharField(max_length=50)
    password = models.CharField(max_length=16)
    question_paper_created = ArrayField(models.CharField(max_length=10))

class student(models.Model):
    student_id = models.CharField(max_length=10)
    student_name = models.CharField(max_length=50)
    pasword = models.CharField(max_length=16)
    student_class = models.CharField(max_length=3)
    question_paper_attempted = ArrayField(models.CharField(max_length=10))

class Question_paper(models.Model):
    question_by_id = ArrayField(models.CharField(max_length=10))
    question_paper_created_by =  ArrayField(models.CharField(max_length=50))
    student_attempted = ArrayField(models.CharField(max_length=50))

