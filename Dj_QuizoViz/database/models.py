from django.db import models

# Create your models here.
class question(models.Model):
    question_id = models.CharField(max_length=10)
    question_text = models.CharField(max_length=500)
    option_a = models.CharField(max_length=500)
    option_b = models.CharField(max_length=500)
    option_c = models.CharField(max_length=500)
    option_d = models.CharField(max_length=500)
    correct_option = models.CharField(max_length=1)
    question_paper = models.ForeignKey("question_paper", on_delete=models.CASCADE)


class teacher(models.Model):
    teacher_id = models.CharField(max_length=10)
    teacher_name = models.CharField(max_length=50)
    password = models.CharField(max_length=16)
    
class question_paper(models.Model):
    question_paper_id = models.CharField(max_length=10)
    teacher_created = models.ForeignKey("teacher", on_delete=models.CASCADE,null = True)
    

    
class student(models.Model):
    student_id = models.CharField(max_length=10)
    student_name = models.CharField(max_length=50)
    pasword = models.CharField(max_length=16)
    student_class = models.CharField(max_length=3)






