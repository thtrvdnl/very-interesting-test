from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('home', views.home, name='home'),
    path('create', views.add_note, name='create'),
]
