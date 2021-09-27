from rest_framework import viewsets
from .models import Song, Artist
from .serializers import SongSerializer, ArtistSerializer

class SongView(viewsets.ModelViewSet):

    queryset = Song.objects.all()
    serializer_class = SongSerializer


class ArtistView(viewsets.ModelViewSet):

    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer