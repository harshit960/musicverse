from django.urls import path
from .views import Home,get_audio_data
urlpatterns = [
    path('', Home , name='MusicVerse'),

    path('player', get_audio_data , name='downloader'),
    
]