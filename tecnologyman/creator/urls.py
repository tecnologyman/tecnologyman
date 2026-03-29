from django.urls import path
from .views import creator_home

urlpatterns = [
    path('', creator_home),
]