from django.urls import path
from weekdays.views import WeekdaysView

urlpatterns = [
    path('week/<str:lang>', WeekdaysView, name='week')

    # path('/en', WeekdaysEnView, name='weekdaysyen'),
    # path('/uz', WeekdaysUzView, name='weekdaysyuz'),
    # path('/ru', WeekdaysRuView, name='weekdaysyru')
]