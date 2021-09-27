from django.db.models import Prefetch
from django.db.models.query_utils import Q
from .decorators import query_debugger
from .models import Artist, Genre, Song, Playlist


@query_debugger
def song_list():

    queryset = Song.objects.all()

    songs = []

    for song in queryset:
        songs.append(
            {
                "id": song.id,
                "title": song.title,
                "artist": song.artist.name
            }
        )
    return songs


@query_debugger
def song_list_select_related():

    queryset = Song.objects.select_related("artist").all()

    songs = []

    for song in queryset:
        songs.append(
            {
                "id": song.id,
                "title": song.title,
                "artist": song.artist.name
            }
        )
    return songs


@query_debugger
def playlist_list():

    queryset = Playlist.objects.all()

    playlists = []
    for playlist in queryset:
        songs = [song.title for song in playlist.songs.all()]
        playlists.append({
            "id" : playlist.id,
            "title": playlist.title,
            "songs": songs
        })
    return playlists


@query_debugger
def playlist_list_prefetch_related():

    queryset = queryset = Playlist.objects.prefetch_related("songs")

    playlists = []
    for playlist in queryset:
        songs = [song.title for song in playlist.songs.all()]
        playlists.append({
            "id" : playlist.id,
            "title": playlist.title,
            "songs": songs
        })
    return playlists