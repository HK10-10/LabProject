from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
     path('', views.home, name='home'),
    path('patient/', views.index, name='lab'),
    path('registration/', views.registration, name='registration'),
    path('lab_login/', views.lab_login, name='lag_login'),
    path('patient_login/', views.patient_login, name='patient_login'),
]
