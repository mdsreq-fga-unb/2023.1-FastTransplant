from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('data', views.data, name='data'),
    path('panel', views.panel, name='panel'),
    path('donators', views.donators, name='donators'),
    path('pacients', views.pacients, name='pacients'),
    path('receivers', views.receivers, name='receivers'),
]