from django.contrib import admin
from .models import Artist, Genre, Playlist, Song

admin.site.register(
    [Artist,
    Genre,
    Playlist, 
    Song]
)
