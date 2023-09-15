from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.views.generic import ListView
from country.models import Countries

# Create your views here.
class CountryListView(ListView):
    # model = Countries # model = Countries = =queryset = Countries.objects.all() 
    # queryset = Countries.objects.all()
    def get_queryset(self): # query set metodi overriding qilinayapti avval yozilgan bu
        try:
            letter = self.request.GET['alphabet']
            queryset = Countries.objects.filter(name__startwith = letter)
        except:
            queryset = Countries.objects.all()
        return queryset
            

    template_name = 'country.html'




