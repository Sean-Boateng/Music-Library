from django.shortcuts import get_object_or_404
from urllib.request import Request
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import SongSerializer
from .models import Song
from rest_framework import status

from songs import serializers



@api_view(['GET', 'POST'])
def song_list(request):
    if request.method == 'GET':
        songs = Song.objects.all()
        serializer = SongSerializer(songs,many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SongSerializer(data = request.data) 
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status= status.HTTP_201_CREATED )
    
        
# This is another way to write the POST code above
    # if serializer.is_valid() == True:
    #     serializer.save()
    #     return Response(serializer.data, status=201)
    # else:
    #     return Response(serializer.errors, status=400)



@api_view(['GET', 'PUT','DELETE'])
def song_details(request, pk):
    songs = get_object_or_404(Song,pk=pk)
    if request.method == 'GET':
        serializer = SongSerializer(songs)
        return Response(serializer.data)

    elif request.method =='PUT':
        serializer = SongSerializer(songs, data=request.data)
        serializer.is_valid(raise_exception=True) 
        serializer.save()
        return Response(serializer.data)
        
    elif request.method == 'DELETE':
        songs.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



    
    


