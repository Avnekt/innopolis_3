# from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView
from todolist.models import todoList
from .serializers import TodoSerializer
from .filters import TodoFilterSet
# from datetime import datetime

from rest_framework import viewsets, mixins
from rest_framework import permissions
from rest_framework.schemas.openapi import AutoSchema

def current_datetime(request):
    now = timezone.now()
    # now = datetime.now()
    html = f'<html><body><h2>{now}</h2><br>{request.user}</body></html>'
    return HttpResponse(html)

class TodolistViewSet(viewsets.ModelViewSet):
    queryset = todoList.objects.all().order_by('-id')
    serializer_class = TodoSerializer
    filterset_class =  TodoFilterSet

    schema = AutoSchema(
        tags=['Tasks'],
        component_name='todoList',
        operation_id_base='todoList',
    )

class MyModelListView(ListView):
    model = todoList
    template_name = 'todo_list.html'

class MyModelUpdateView(UpdateView):
    model = todoList
    fields = [
        'taskName',
        'taskCompleted',
    ]
    template_name = 'todo_update_form.html'
    success_url = '/todolist/'

class MyModelCreateView(CreateView):
    model = todoList
    fields = [
        'taskName',
    ]
    template_name = 'todo_create_form.html'
    success_url = '/todolist/'

class MyModelDeleteView(DeleteView):
    model = todoList
    template_name = 'todo_delete_form.html'
    success_url = '/todolist/'

class MyModelDetailView(DetailView):
    model = todoList
    template_name = 'todo_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context