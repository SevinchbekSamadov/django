from django.contrib import admin
from .models import UzbDistricts
# Register your models here.

class DistrictAdmin(admin.ModelAdmin):
    list_display = ('id','district_name_uz', 'district_name_en')
    search_fields = ('district_name_uz','district_name_ru')
    list_filter = ['id']
admin.site.register(UzbDistricts,DistrictAdmin)
