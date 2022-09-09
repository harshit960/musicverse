from django.urls import path
from .views import Home,get_audio_data,searchRequest,managePlaylist
urlpatterns = [
    path('', Home , name='MusicVerse'),

    path('player', get_audio_data , name='downloader'),
    path('search', searchRequest , name='Search page'),
    path('playlist', managePlaylist,name='Playlist')
    
]