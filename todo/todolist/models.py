from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import Group

class todoList(models.Model):
    
    taskName = models.CharField(max_length=150, help_text="Заголовок задачи")
    taskCreatedTime = models.DateTimeField(auto_now=True, help_text="Время создания задачи")
    taskCompleted = models.BooleanField(default=False, help_text="Отметка о выполнении задачи")
    taskCompleteTime = models.DateTimeField(
        default=None,
        auto_now=False,
        blank=True,
        null=True,
        help_text="Время завершения задачи"
    )
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='created_tasks',
        help_text='Пользователь, создавший задание',
    )

    def save(self, *args, **kwargs) -> None:
        if not self.taskCompleted and self.taskCompleteTime:
            self.taskCompleteTime = None
        elif self.taskCompleted and self.taskCompleteTime is None:
            self.taskCompleteTime = timezone.now()
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f'Task {self.id}|{self.taskName}|{self.taskCompleted}'