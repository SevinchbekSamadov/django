from django.urls import path
from country.views import CountryListView

urlpatterns = [
    path('',CountryListView.as_view() )

]