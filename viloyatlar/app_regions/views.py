from typing import Any
from django.db.models.query import QuerySet
from django.views.generic import ListView
from .models import UzbRegions, UzbDistricts
from django.db.models import F
from django.http import HttpResponse
# Create your views here.

class RegionsListView(ListView):
    # model = UzbRegions
    template_name = 'regions.html'

    def get_queryset(self):
        try:
            lang = self.request.session['lang']
        except:
            lang = 'uz'
            self.request.session['lang'] = 'uz'
        queryset = UzbRegions.objects.all().values('id','region_name_' + lang).annotate(region_name = F('region_name_' + lang))
        return queryset
    
class UzbDistrictsListView(ListView):
    template_name = 'districts.html'

    def get_queryset(self):
        try:
            pk = self.request.GET['region']
        except:
            pk = 1
        try:
            lang = self.request.session['lsng']
        except:
            lang = 'uz'
            self.request.session['lang'] = 'uz'
        queryset = UzbRegions.objects.all().values('id','district_name_' + lang).annotate(district_name = F('district_name_' + lang))
        return queryset
    
def setlang(request, lang):
    request.session['lang'] = lang
    return HttpResponse('OK')

