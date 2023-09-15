from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView
from pupils.models import Pupils1, Pupils2

class PupilsView(ListView):
    model = Pupils1
    template_name = 'pupils.html'

    # def __str__(request,lang):
    #     if lang =='first':
    #         model = Pupils1
    #     else:
    #         model = Pupils2
    # template_name = 'pupils.html'


# Create your views here.
# def PupilsView(request, lang):
#     context_first = {'pupil': "1-oy", 'data':Pupils1.objects.all()}
#     context_second = {'pupil': "2-oy", 'data':Pupils2.objects.all}

#     if lang == 'first':
#         context =context_first
#     else:
#         context = context_second
#     return render(request,'pupils.html',context)
