from django.urls import path
from . import views

urlpatterns = [
    path('', views.registration, name='registration'),
    path('info/', views.info, name='info'),
]