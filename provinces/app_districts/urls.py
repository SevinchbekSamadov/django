from django.urls import path
from .views import ViloyatView,TumanView, setlang

urlpatterns = [
    path('',ViloyatView.as_view()),
    path('setlang/<str:lang>', setlang),
    path('tuman/',TumanView.as_view(), name='tuman')
]
