from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('receivers/', views.receiver_list, name='receivers'),
    path('receivers/new/', views.receiver_new, name='receiver_new'),
    path('donators/', views.donator_list, name='donators'),
    path('donators/new/', views.donator_new, name='donator_new'),
    path('donators/new/confirm', views.donator_new_confirm, name='donator_new_confirm'),
    # path('atualizar_dados/', atualizar_dados, name='atualizar_dados'),
    # path('recep/', recep, name='recep'),
    # path('new', views.new, name='new'),
    # path('new/confirm', views.update_data, name='update_data'),
    # path('receiver/new', views.new_receiver, name='new_receiver')
]