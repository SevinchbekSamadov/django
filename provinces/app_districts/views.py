from django.views.generic import ListView
from .models import Viloyat, Tuman
from django.http import HttpResponse
from django.db.models import F

# Create your views here.

class ViloyatView(ListView):
    model = Viloyat
    template_name = 'viloyat.html'

class TumanView(ListView):
    # model = Tuman
    template_name = 'tuman.html'
    def get_queryset(self):
        try:
            lang = self.request.session['lang']
        except:
            lang = 'uz'
            self.request.session['lang'] = 'uz'
        queryset = Tuman.objects.all().values('tuman_' + lang).annotate(tuman = F('tuman_' + lang))
        return queryset
def setlang(request, lang):
    try:
        request.session['lang'] = lang
        return HttpResponse('OK')
    except:
        return HttpResponse('Error')
