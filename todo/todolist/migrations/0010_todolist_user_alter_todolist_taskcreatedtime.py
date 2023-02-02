# Generated by Django 4.1.5 on 2023-01-31 08:25

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("todolist", "0009_alter_todolist_taskcompletetime_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="todolist",
            name="user",
            field=models.ForeignKey(
                blank=True,
                help_text="Пользователь, создавший задание",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="created_tasks",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="todolist",
            name="taskCreatedTime",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 1, 31, 8, 25, 47, 541049, tzinfo=datetime.timezone.utc
                ),
                help_text="Время создания задачи",
            ),
        ),
    ]