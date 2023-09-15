from django.urls import path
from pupils.views import PupilsView

urlpatterns = [
    path('pupils/first', PupilsView.as_view(), name='pupils')

]