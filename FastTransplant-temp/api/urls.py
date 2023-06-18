from django.urls import path, include
from . import views

urlpatterns = [
    path('pacient/add', views.create_pacient, name='create_pacient'),
    path('pacient/list', views.pacient_list, name='pacient_list'),
    path('pacient/update', views.update_pacient, name='update_pacient'),
    path('pacient/delete', views.delete_pacient, name='detete_pacient'),
    path('organ/add', views.create_organ_report, name='create_organ_report'),
]
