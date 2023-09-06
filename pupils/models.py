from django.db import models

# Create your models here.

class Pupils1(models.Model):
    p_name = models.CharField(max_length=100, verbose_name='name of pupil')
    score = models.IntegerField(verbose_name='ball of pupil')
class Pupils2(models.Model):
    p_name = models.CharField(max_length=100, verbose_name='name of pupil')
    score = models.IntegerField(verbose_name='ball of pupil')
