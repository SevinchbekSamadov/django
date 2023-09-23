from django.db import models

# Create your models here.

class My_books(models.Model):
    book_name_uz = models.CharField(max_length=200)
    book_name_en = models.CharField(max_length=200)

    class Meta:
        db_table = 'books'
    
    
class About_books(models.Model):
    about_uz = models.CharField(max_length=255)
    about_en = models.CharField(max_length=255)
    about_id = models.ForeignKey(My_books, on_delete=models.CASCADE)

    class Meta:
        db_table = 'about'