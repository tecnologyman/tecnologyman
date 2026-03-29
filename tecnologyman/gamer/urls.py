from django.urls import path
from . import views

urlpatterns = [
    path('', views.gamer_home, name='gamer_home'),
    path('<slug:slug>/', views.game_detail, name='game_detail'),
]