from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns

from . import views


urlpatterns = {
    path('items', views.manage_items, name="manage_items"),
    path('items/<slug:key>', views.manage_item, name="single_item")
}
urlpatterns = format_suffix_patterns(urlpatterns)
