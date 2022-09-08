from django.urls import path
from .views import *
urlpatterns = [
    path('', Home , name='MusicVerse'),

    path('player', get_audio_data , name='downloader'),
    
]