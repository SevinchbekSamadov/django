from django.db import models

# Create your models here.

class Pupils(models.Model):
    first_name = models.CharField(max_length=25, verbose_name='ism')
    last_name = models.CharField(max_length=25, verbose_name='familiya')
    exam_mark = models.IntegerField(verbose_name='imtihon bahosi')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"