from . import views
from django.urls import path 

urlpatterns = [
    path('', views.register),
    path('register' , views.register),
    path('regi' , views.regi),
    path('login' , views.login),
    path('logi' , views.logi),
    path('show' , views.show),
    
]
