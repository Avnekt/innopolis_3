from django_filters import rest_framework as dj_filters
from .models import todoList


class TodoFilterSet(dj_filters.FilterSet):
    """Набор фильров для представления для модели todoList."""

    title = dj_filters.CharFilter(field_name="taskName", lookup_expr="icontains")

    order_by_field = "ordering"

    class Meta:
        model = todoList
        fields = [
            "id",
            "taskName",
        ]
