from django.contrib import admin
from todolist.models import todoList
from django.db import models
from django.utils import timezone

@admin.action(description="Отменить выполнение задач")
def cancel_complete(self, request, queryset: models.QuerySet):
    queryset.update(taskCompleted=False, taskCompleteTime=None)

@admin.action(description="Задачи выполнены")
def make_complete(self, request, queryset: models.QuerySet):
    queryset.update(taskCompleted=True, taskCompleteTime=timezone.now())

@admin.register(todoList)
class todoListAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "taskName",
        "taskCompleted",
    ]
    actions = [
        cancel_complete,
        make_complete
    ]
