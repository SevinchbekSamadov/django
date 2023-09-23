from django.db import models

# Create your models here.

class Books(models.Model):
    book_name_uz = models.CharField(max_length=255, verbose_name='kitobning nomi')
    book_name_en = models.CharField(max_length=255, verbose_name='name of book')
    about_uz = models.CharField(max_length=255, verbose_name='kitob haqida')
    about_en = models.CharField(max_length=255, verbose_name='about book')

    def __str__(self):
        return self.book_name_uz
    
    class Meta:
        db_table = 'books'