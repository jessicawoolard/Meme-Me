from django.contrib import admin
from django.urls import path

from .api import MemeViewSet

urlpatterns = [
    path('api/meme/', MemeViewSet.as_view({
       'get': 'list',
       'post': 'create',
    }), name='meme_api'),
]
