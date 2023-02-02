# Generated by Django 4.1.5 on 2023-01-31 06:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todolist", "0006_alter_todolist_taskcompletetime_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="todolist",
            name="taskCompleteTime",
            field=models.DateTimeField(
                default=None, help_text="Время завершения задачи"
            ),
        ),
        migrations.AlterField(
            model_name="todolist",
            name="taskCompleted",
            field=models.BooleanField(
                default=False, help_text="Отметка о выполнении задачи"
            ),
        ),
        migrations.AlterField(
            model_name="todolist",
            name="taskCreatedTime",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 1, 31, 6, 18, 26, 648959, tzinfo=datetime.timezone.utc
                ),
                help_text="Время создания задачи",
            ),
        ),
    ]