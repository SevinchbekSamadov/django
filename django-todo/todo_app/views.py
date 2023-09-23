from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Todos
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
class TodoListView(ListView):
    # model = Todos
    template_name = 'C:\\Users\\user\\Desktop\\takrorlash\\django-todo\\templates\\todos\\list.html'
    def get_queryset(self):
        try:
            fk = self.kwargs['fk']
            queryset = Todos.objects.filter(user_id= fk)
            return queryset
        except:
            queryset = Todos.objects.all()
        return queryset
    


class NewCreateView(LoginRequiredMixin,CreateView):
    model = Todos
    template_name = 'C:\\Users\\user\\Desktop\\takrorlash\\django-todo\\templates\\todos\\todos_new.html'
    fields = ('title', 'description', 'start_time', 'end_time', 'status')
    success_url = '/user/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)