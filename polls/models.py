from django.db import models

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_lenght=200)
    pub_date = models.DateTimeField(auto_add_now=True)



class Choices(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_answer = models.CharField(max_length=20)
    votes = models.IntegerField(default=0)