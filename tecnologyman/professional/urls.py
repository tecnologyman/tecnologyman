from django.urls import path
from .views import professional_home

urlpatterns = [
    path('', professional_home),
]