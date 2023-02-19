from rest_framework.routers import DefaultRouter
from .views import TodolistViewSet

# router = DefaultRouter(trailing_slash=False)
router = DefaultRouter()

app_name = "todolistapp"


router.register(
    prefix="tasks",
    viewset=TodolistViewSet,
    basename="tasks",
)

urlpatterns = router.urls