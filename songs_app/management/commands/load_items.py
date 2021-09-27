import random
from typing import Any, Optional
from django.core.management.base import BaseCommand
from songs_app.models import Genre, Song, Playlist, Artist


GENRES = (
    "Rock", "Pop", "Jazz", "Indie", "Britpop", "Lo-Fi", "Metal"
)

ARTISTS = (
    "Nirvana", "Jamiroquai", "Bill Withers", "No Doubt", "Nick Cave"
)

YEARS = [random.randint(1950, 2021) for i in range(30)]


class Command(BaseCommand):

    def handle(self, *args: Any, **options: Any) -> Optional[str]:
        
        Genre.objects.all().delete()
        Playlist.objects.all().delete()
        Song.objects.all().delete()
        Artist.objects.all().delete()

        genres = [Genre(name=genre) for genre in GENRES]
        Genre.objects.bulk_create(genres)

        artists = [Artist(name=artist_name) for artist_name in ARTISTS]
        Artist.objects.bulk_create(artists)


        songs = []
        for artist in Artist.objects.all():
            for i in range(10):
                songs.append(Song(
                    title="Song #{}".format(i+1),
                    artist=artist
                ))
        Song.objects.bulk_create(songs)


        songs = list(set(Song.objects.all()))
        for i in range(10):
            try:
                temp_songs = [songs.pop(0) for i in range(10)]
                genres = Genre.objects.all()
                playlist = Playlist.objects.create(
                    title="Playlist #{}".format(i+1),
                    year=random.choice(YEARS),
                    genre=random.choice(genres)
                )
                playlist.songs.set(temp_songs)
                playlist.save()
            except IndexError:
                break