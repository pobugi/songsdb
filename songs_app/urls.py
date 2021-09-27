from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()

router.register('songs', views.SongView)
router.register('artists', views.ArtistView)

urlpatterns = [
    path('', include(router.urls)),
]