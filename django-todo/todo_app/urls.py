from django.urls import path
from .views import TodoListView, NewCreateView

urlpatterns = [
    path('list/<int:fk>/', TodoListView.as_view(), name  = 'todo-list'),
    path('new', NewCreateView.as_view(), name  = 'todo-new')
]
