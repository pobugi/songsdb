from django.db import models
from datetime import date


class Artist(models.Model):

    name = models.CharField("Artist name", max_length=100)
    description = models.TextField("Artist description", default="no description")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Artist"
        verbose_name_plural = "Artists"


class Genre(models.Model):

    name = models.CharField("Genre name", max_length=100)
    description = models.TextField("Genre description", default="no description")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Genre"
        verbose_name_plural = "Genres"


class Album(models.Model):

    title = models.CharField("Album title", max_length=100)
    description = models.TextField("Album description", default="no description")
    year = models.IntegerField("Album release year")

    genres = models.ManyToManyField(Genre, verbose_name="genres")
    artists = models.ManyToManyField(Artist, verbose_name="artists")

    def __str__(self):
        return "{} ({})".format(self.title, self.year)

    class Meta:
        verbose_name = "Album"
        verbose_name_plural = "Albums"


class Song(models.Model):

    title = models.CharField("Song title", max_length=100) 
    album = models.ForeignKey(Album, verbose_name="album", on_delete=models.SET_NULL, null=True)
    artists = models.ManyToManyField(Artist, verbose_name="artists")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Song"
        verbose_name_plural = "Songs"
