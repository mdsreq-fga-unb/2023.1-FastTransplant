from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('receivers/', views.receiver_list, name='receivers'),
    path('receivers/new/', views.receiver_new, name='receiver_new'),
    path('receivers/delete/<int:pk>/', views.receiver_delete, name='receiver_delete'),
    path('receivers/update/<int:pk>/', views.receiver_update, name='receiver_update'),
    path('donators/', views.donator_list, name='donators'),
    path('donators/new/', views.donator_new, name='donator_new'),
    path('donators/new/confirm', views.donator_new_confirm, name='donator_new_confirm'),
    path('donators/delete/<int:pk>/', views.donator_delete, name='donator_delete'),
    path('donators/update/<int:pk>/', views.donator_update, name='donator_update'),
]