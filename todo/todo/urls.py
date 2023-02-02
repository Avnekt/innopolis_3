"""todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from todolist.views import current_datetime
from todolist.views import MyModelListView, MyModelUpdateView, MyModelCreateView, MyModelDeleteView, MyModelDetailView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("time/", current_datetime),
    path("todolist/", MyModelListView.as_view()),
    path("todoupdate/<int:pk>", MyModelUpdateView.as_view()),
    path("todocreate/", MyModelCreateView.as_view()),
    path("tododelete/<int:pk>", MyModelDeleteView.as_view()),
    path('tododetail/<int:pk>', MyModelDetailView.as_view()),
]
