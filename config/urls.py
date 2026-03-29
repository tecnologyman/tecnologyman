from django.contrib import admin
from django.urls import path, include
from core.views import home

urlpatterns = [
    path('admin/', admin.site.urls),   # ← ESTO SE MANTIENE
    path('', home),
    path('gamer/', include('gamer.urls')),
    path('creator/', include('creator.urls')),
    path('professional/', include('professional.urls')),
]