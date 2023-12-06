from django.contrib import admin
from django.urls import path 
from meus_games.views import sobre

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sobre/', sobre),
]
