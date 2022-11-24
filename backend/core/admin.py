from django.contrib import admin
from .models import Album, Singer, Song

# Register your models here.


admin.site.register(Singer)


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display=["singer", "song_title", "volume", "album", "is_favorite"]
    list_filter=["singer", "volume", "album", "is_favorite"]


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display=["volume", "singer", "album_title"]
    list_filter=["volume", "singer", "album_title"]
    

