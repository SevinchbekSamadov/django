from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Todos(models.Model):
    title = models.CharField(max_length=255, verbose_name='title')
    description = models.TextField( verbose_name="full text to do")
    start_time = models.DateField(verbose_name="start time")
    end_time = models.DateTimeField(verbose_name="end time")
    statuses = {
        ('a', 'active'),
        ('o', 'done'),
        ('n', 'not yet'),
    }
    status = models.CharField(max_length=15, verbose_name='Status', choices=statuses)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='author', null=True, blank=True)

    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'todo_list'
        ordering = ['start_time', 'title']