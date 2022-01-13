
from django.urls import include, path
from rest_framework import routers
from . import views
from .models import Patient


urlpatterns = [
    path('list/', views.PatientList.as_view()),
]