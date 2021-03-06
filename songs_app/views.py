from rest_framework import viewsets
from .models import Song, Artist, Genre, Playlist
from .serializers import SongSerializer, ArtistSerializer, GenreSerializer, PlaylistSerializer

class SongView(viewsets.ModelViewSet):

    # queryset = Song.objects.all()
    queryset = Song.objects.select_related("artist").all()
    serializer_class = SongSerializer


class ArtistView(viewsets.ModelViewSet):

    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class GenreView(viewsets.ModelViewSet):

    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class PlaylistView(viewsets.ModelViewSet):

    # queryset = Playlist.objects.all()
    queryset = Playlist.objects.prefetch_related("songs")
    serializer_class = PlaylistSerializer