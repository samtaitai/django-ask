import datetime
from django.db import models
from django import forms
from django.utils import timezone
from django.conf import settings

class Question(models.Model):
    question_text = models.TextField()
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

class Answer(models.Model):
    author = models.CharField(max_length=200, default="admin",)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.TextField()

    def __str__(self):
        return self.answer_text
