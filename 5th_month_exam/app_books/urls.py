from django.urls import path
from .views import setLanguage, BooksView, AboutView

urlpatterns = [
    path('setLang/<str:lang>', setLanguage),
    path('about', AboutView.as_view(), name='about'),
    path('',BooksView.as_view())
    
]
