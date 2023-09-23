from django.urls import path
from .views import RegionsListView, setlang, UzbDistrictsListView

urlpatterns = [
    path('setlang/<str:lang>', setlang),
    path('districts/', UzbDistrictsListView.as_view(), name='districts' ),
    path('', RegionsListView.as_view() ),
]   