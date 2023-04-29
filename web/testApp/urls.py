from django.urls import path 
from . import views

urlpatterns = [
    path('hey', views.testPage)
]