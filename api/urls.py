from django.urls import path
from . import views
from .views import upload_pdf

urlpatterns = [
    path('', views.index, name='index'),
    path('data', views.data, name='data'),
    path('panel', views.panel, name='panel'),
    path('donators', views.donator_list, name='donators'),
    path('patients', views.patient_list, name='patient_list'),
    path('patients/create', views.patient_create, name='patient_create'),
    path('patients/update/<int:pk>', views.patient_update, name='patient_update'),
    path('patients/delete/<int:pk>', views.patient_delete, name='patient_delete'),
    path('receivers', views.receiver_list, name='receiver_list'),
    path('receivers/create', views.receiver_create, name='receiver_create'),
    path('receivers/update/<int:pk>', views.receiver_update, name='receiver_update'),
    path('receivers/delete/<int:pk>', views.receiver_delete, name='receiver_delete'),
    path('patients/', upload_pdf, name='upload_pdf'),
]