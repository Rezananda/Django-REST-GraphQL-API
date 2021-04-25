from django.urls import path
from . import views

urlpatterns = [
    path('actor', views.get_actor, name='get_actor'),
    path('director', views.get_director, name='get_actor'),
    path('movie', views.get_movie, name='get_actor'),
]