from django.core.management.base import BaseCommand
from songs_app.db_queries import song_list_select_related, song_list, playlist_list, playlist_list_prefetch_related


class Command(BaseCommand):

    def handle(self, *args, **options):
        song_list()
        song_list_select_related()
        playlist_list()
        playlist_list_prefetch_related()