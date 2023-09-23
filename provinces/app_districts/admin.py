from django.contrib import admin
from .models import Tuman

# Register your models here.
class TumanAdmin(admin.ModelAdmin):
    list_display = ('id','tuman_uz','tuman_en')
    search_fields = ('id', 'tuman_uz')
admin.site.register(Tuman)