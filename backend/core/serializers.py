
from rest_framework import serializers
from .models import Song, Album, Singer




class SongCreationSerializer(serializers.ModelSerializer):
   
    song=serializers.FileField( allow_empty_file=False)
    
    class Meta:
        model=Song
        fields="__all__"
        



class AlbumCreationSerializer(serializers.ModelSerializer):
    
    songs=SongCreationSerializer(required=False, many=True)
    
    volume=serializers.IntegerField( min_value=1, max_value=30)
    
    album_title=serializers.CharField(max_length=100)
    
    album_logo=serializers.ImageField( allow_empty_file=True)
    
    class Meta:
        model=Album
        fields="__all__"
        
        


class SingerCreationSerializer(serializers.ModelSerializer):
    
    songs=SongCreationSerializer(required=False, read_only=False,  many=True)
    
    albums=AlbumCreationSerializer(required=False, read_only=False, many=True)
      
    
    class Meta:
        model=Singer
        fields="__all__"
        
    
  








        
    
    