from django.urls import path
from .views import RimView

urlpatterns = [
    path('rim', RimView.as_view()),
]