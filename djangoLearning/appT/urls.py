from django.urls import path
from . import views
urlpatterns = [
    path('/demo2', views.demo),
    path('/fk2', views.demo2)
]
