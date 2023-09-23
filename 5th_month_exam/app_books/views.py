from typing import Any
from django.db.models.query import QuerySet
from django.views.generic import ListView
from .models import My_books, About_books
from django.db.models import F
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class BooksView(LoginRequiredMixin,ListView):
    # model = My_books
    template_name = 'book.html'

    def get_queryset(self):
        try:
            lang = self.request.session['lang']
        except:
            lang = 'uz'
            self.request.session['lang'] = 'uz'

        queryset = My_books.objects.all().values('id', 'book_name_' + lang).annotate(book_name=F('book_name_'+lang))
        return queryset
    
class AboutView(ListView):
    template_name = 'about.html'

    def get_queryset(self):
        try:
            pk = self.request.GET['books']
        except:
            pk = 1

        try:
            lang = self.request.session['lang']
        except:
            lang = 'uz'
            self.request.session['lang'] = 'uz'

        queryset = About_books.objects.filter(about_id=pk).values('id', 'about_' + lang).annotate(about=F('about_'+lang))
        return queryset

def setLanguage(request, lang):
    request.session['lang'] = lang
    return HttpResponse('OK')
    