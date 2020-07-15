from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('add_request', views.add_request, name="add_request"),
]