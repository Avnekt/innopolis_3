# from django.contrib.auth.models import User, Group
from todolist.models import todoList
from rest_framework import serializers


# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ['url', 'username', 'email', 'groups']


# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Group
#         fields = ['url', 'name']

class NonModelSerializer(serializers.Serializer):
    """Сериализатор с не-модельными полями."""


class TodoSerializer(serializers.ModelSerializer):
    """Сериализатор для модели TodoList."""


    class Meta:
        model = todoList
        read_only_fields = ["id"]
        fields = read_only_fields + ["taskName", "taskCreatedTime", "taskCompleted", "taskCompleteTime"]

    def to_internal_value(self, data):
        if self.context["request"]._request.method == "POST":
            if not data.get("taskName"):
                data["taskName"] = "default_task"
        return super().to_internal_value(data)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        return representation