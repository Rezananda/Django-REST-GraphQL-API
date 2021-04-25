from django.urls import path
from . import views

urlpatterns = [
    path('bca/api/v1/balance', views.balance, name='balance'),
    path('bca/api/v1/statement', views.statement, name='statement'),
    path('bca/api/v1/graphql', views.getMovie, name='getMovie'),
]