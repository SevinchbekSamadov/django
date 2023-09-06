from django.urls import path
from themes.views import ShowLessonsView

urlpatterns = [
    path('', ShowLessonsView.as_view())
]