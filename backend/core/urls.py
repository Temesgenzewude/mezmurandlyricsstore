
from django.urls import path

from .views import SingerCreateListView, SingerDetailView, SongCreateListView, SongDetailView, AlbumCreateListView, AlbumDetailView

urlpatterns=[
    path('singers/', SingerCreateListView.as_view(), name='singers'),
    path('singers/<int:singer_id>/', SingerDetailView.as_view(), name='singer_detail'),
    path('songs/', SongCreateListView.as_view(), name='songs'),
    path('songs/<int:song_id>/', SongDetailView.as_view(), name='song_detail'),
    path('albums/', AlbumCreateListView.as_view(), name='albums'),
    path('albums/<int:album_id>/', AlbumDetailView.as_view(), name='album_detail'),
    
    ]