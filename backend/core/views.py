from django.shortcuts import render, get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes


from .serializers import SingerCreationSerializer, SongCreationSerializer, AlbumCreationSerializer

from .models import Song, Singer, Album




# Create your views here.

class SingerCreateListView(generics.GenericAPIView):
    serializer_class=SingerCreationSerializer
    queryset=Singer.objects.all()
    
    def get(self, request):
        
        singers=Singer.objects.all()
        
        serializer=self.serializer_class(instance=singers, many=True)
        
        
        return Response(data=serializer.data, status=status.HTTP_200_OK)
          
        
   
    def post(self, request):
        data=request.data
        
        serializer=self.serializer_class(data=data)
        
        if serializer.is_valid():
            serializer.save()
            
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        

class SingerDetailView(generics.GenericAPIView):
    
    serializer_class=SingerCreationSerializer

    
    def get(self, request, singer_id):
        
        singer=get_object_or_404(Singer, pk=singer_id)
        serializer=self.serializer_class(instance=singer)
        
        return Response(data=serializer.data, status=status.HTTP_200_OK)
        
        
    
    def put(self, request, singer_id):
        
        data=request.data
        singer=get_object_or_404(Singer, pk=singer_id)
        
        serializer=self.serializer_class(data=data, instance=singer)
        
        if serializer.is_valid():
            serializer.save()

            return Response(data=serializer.data, status=status.HTTP_200_OK)
        
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
        
        
        
    
    def delete(self, request, singer_id):
        singer=get_object_or_404(Singer, pk=singer_id)
        
        singer.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)
         
    




class SongCreateListView(generics.GenericAPIView):
    serializer_class=SongCreationSerializer
    
    queryset=Song.objects.all()
    
    def get(self, request):
        
        songs=Song.objects.all()
        
        serializer=self.serializer_class(instance=songs, many=True)
        
        
        return Response(data=serializer.data, status=status.HTTP_200_OK)
          
        
   
    def post(self, request):
        data=request.data
        
        serializer=self.serializer_class(data=data)
        
        if serializer.is_valid():
            serializer.save()
            
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    

class SongDetailView(generics.GenericAPIView):
    serializer_class=SongCreationSerializer
    
    
    def get(self, request, song_id):
        
        song=get_object_or_404(Singer, pk=song_id)
        serializer=self.serializer_class(instance=song)
        
        return Response(data=serializer.data, status=status.HTTP_200_OK)
        
        
    
    def put(self, request, song_id):
        
        data=request.data
        song=get_object_or_404(Singer, pk=song_id)
        
        serializer=self.serializer_class(data=data, instance=song)
        
        if serializer.is_valid():
            serializer.save()

            return Response(data=serializer.data, status=status.HTTP_200_OK)
        
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
        
        
        
    
    def delete(self, request, song_id):
        song=get_object_or_404(Singer, pk=song_id)
        
        song.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
    
    
    
class AlbumCreateListView(generics.GenericAPIView):
    serializer_class=AlbumCreationSerializer
    
    queryset=Album.objects.all()
    
    def get(self, request):
        
        albums=Album.objects.all()
        
        serializer=self.serializer_class(instance=albums, many=True)
        
        
        return Response(data=serializer.data, status=status.HTTP_200_OK)
          
        
   
    def post(self, request):
        data=request.data
        
        serializer=self.serializer_class(data=data)
        
        if serializer.is_valid():
            serializer.save()
            
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AlbumDetailView(generics.GenericAPIView):
    serializer_class=AlbumCreationSerializer
    
    
    
    def get(self, request, album_id):
        
        album=get_object_or_404(Singer, pk=album_id)
        serializer=self.serializer_class(instance=album)
        
        return Response(data=serializer.data, status=status.HTTP_200_OK)
        
        
    
    def put(self, request, album_id):
        
        data=request.data
        album=get_object_or_404(Singer, pk=album_id)
        
        serializer=self.serializer_class(data=data, instance=album)
        
        if serializer.is_valid():
            serializer.save()

            return Response(data=serializer.data, status=status.HTTP_200_OK)
        
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
        
        
        
    
    def delete(self, request, album_id):
        album=get_object_or_404(Singer, pk=album_id)
        
        album.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)
