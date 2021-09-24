from django.contrib import admin
from .models import Artist, Genre, Album, Song

admin.site.register(
    [Artist,
    Genre,
    Album, 
    Song]
)
