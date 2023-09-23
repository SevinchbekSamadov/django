from django.urls import path
from .views import PupilsView

urlpatterns = [
    path('',PupilsView.as_view())
]
