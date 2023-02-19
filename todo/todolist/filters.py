from django_filters import rest_framework as dj_filters
from .models import todoList


class TodoFilterSet(dj_filters.FilterSet):
    """Набор фильров для представления для модели todoList."""
    
    task = dj_filters.CharFilter(field_name="taskName", lookup_expr="icontains")
    is_active = dj_filters.BooleanFilter(field_name="taskCompleted", exclude=True)

    order_by_field = "ordering"

    class Meta:
        model = todoList
        fields = [
            "id",
            "taskName",
        ]
    
    def invert_value(self, obj, *argvs):
        try:
            eval(obj.lookup_expr)
            return not eval(obj.lookup_expr)
        except:
             return obj.lookup_expr
