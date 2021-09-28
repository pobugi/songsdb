from rest_framework import serializers
from .models import Song, Artist, Genre, Playlist


class ArtistSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Artist
        fields = ('url', 'name', 'description')

class SongSerializer(serializers.HyperlinkedModelSerializer):

    # author = ArtistSerializer(source='artist')
    artist = serializers.StringRelatedField()
    class Meta:
        model = Song
        fields = '__all__'


class GenreSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Genre
        fields = ('url', 'name', 'description')


class PlaylistSerializer(serializers.HyperlinkedModelSerializer):

    genre = serializers.StringRelatedField()
    songs = serializers.StringRelatedField(many=True)

    class Meta:
        model = Playlist
        fields = ('url', 'title', 'description', 'year', 'genre', 'songs')

