from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('add_request/', views.add_request, name="add_request"),
    path('upload/', views.upload, name="upload"),
]