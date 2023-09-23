from django.contrib import admin
from .models import Todos
# Register your models here.


class TodosAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'status')
    search_fields = ('tite','description')
admin.site.register(Todos, TodosAdmin)