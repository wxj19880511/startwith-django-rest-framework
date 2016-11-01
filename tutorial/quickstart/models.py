from __future__ import unicode_literals

from django.db import models

# Create your models here.
class FooModel(models.Model):
    question_text1 = models.CharField(max_length=200)
    question_text2 = models.CharField(max_length=200)