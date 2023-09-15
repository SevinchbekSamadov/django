from django.db import models

# Create your models here.

class Countries(models.Model):
    name = models.CharField(max_length=255,verbose_name='country_name')
    population = models.IntegerField(verbose_name='population')
    area = models.FloatField(verbose_name='area of country')
    density = models.FloatField(verbose_name='density of country')

    class Meta:
        db_table = 'countries'

    
