from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('compatibility/', views.compatibility, name='compatibility'),
    path('donators/', views.donators_list, name='donators_list'),
    path('donators/create/', views.donators_create, name='donators_create'),
    path('donators/create/pdf', views.donators_create_pdf, name='donators_create_pdf'),
    path('donators/<int:id>', views.donators_read, name='donators_read'),
    path('donators/update/<int:id>', views.donators_update, name='donators_update'),
    path('donators/delete/<int:id>', views.donators_delete, name='donators_delete'),
    path('error/', views.error, name='error'),
    path('log/', views.log, name='log'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('receivers/', views.receivers_list, name='receivers_list'),
    path('receivers/create/', views.receivers_create, name='receivers_create'),
    path('receivers/create/pdf', views.receivers_create_pdf, name='receivers_create_pdf'),
    path('receivers/<int:id>', views.receivers_read, name='receivers_read'),
    path('receivers/update/<int:id>', views.receivers_update, name='receivers_update'),
    path('receivers/delete/<int:id>', views.receivers_delete, name='receivers_delete'),
    path('recover/', views.recover, name='recover'),
    path('reports/', views.reports, name='reports'),
    path('search/', views.search, name='search'),
    path('users/', views.users, name='users'),
]
