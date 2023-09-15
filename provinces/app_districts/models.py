from django.db import models

# Create your models here.

class Viloyat(models.Model):
    viloyat_ID = models.IntegerField(primary_key=True)
    viloyat = models.CharField(max_length=255)


    class Meta:
        db_table = 'viloyatlar'

class Tuman(models.Model):
    tuman_uz = models.CharField(max_length=255)
    tuman_en = models.CharField(max_length=255)
    tuman_ru = models.CharField(max_length=255)
    tumen_id = models.ForeignKey(Viloyat,on_delete=models.CASCADE)

    class Meta:
        db_table = 'tumanlar'

# def __str__(self):
#     return str(self.engine) + "  (ref:" + str(self.ref) + ")"
