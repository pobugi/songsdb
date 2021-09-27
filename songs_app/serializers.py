from rest_framework import serializers
from .models import Song, Artist, Genre, Playlist


class ArtistSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Artist
        fields = ('url', 'name', 'description')

class SongSerializer(serializers.HyperlinkedModelSerializer):

    author = ArtistSerializer(source='artist')
    class Meta:
        model = Song
        fields = ('url', 'title', "author")


class GenreSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Genre
        fields = ('url', 'name', 'description')


class PlaylistSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Playlist
        fields = ('url', 'title', 'description', 'year', 'genre', 'songs')

