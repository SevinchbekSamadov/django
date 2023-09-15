from django.db import models

# Create your models here.

class Lesson(models.Model):
    lesson_title = models.CharField(max_length=100, verbose_name='Lesson')
