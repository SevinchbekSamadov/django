from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.

# def WeekdaysEnView(request):
#     english = """Monday Tuesday Wednesday Thursday Friday Satruday Sunday"""
#     return HttpResponse(english)

# def WeekdaysUzView(request):
#     uzbek ="""Dushanba Seshanba Chorshanba Payshanba Juma Shanba Yakshanba"""
#     return HttpResponse(uzbek)

# def WeekdaysRuView(request):
#     russian = """poledenlik"""
#     return HttpResponse(russian)

def WeekdaysView(request, lang):
    context_uz = {'week': 'Hafta kunlari', 'data': ['Yak','Du','Se']}
    context_en = {'week': 'Week days', 'data':['Mon','Tu','We']}
    context_ru = {'week': 'Rus tilida', 'data': ['pon','vto','chet']}

    if lang  == 'en':
        context = context_en
    elif lang == 'ru':
        context = context_ru
    else:
        context = context_uz

    return render(request,'home.html', context)