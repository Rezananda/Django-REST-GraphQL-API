from django.shortcuts import render
from graphqltest.models import Actor, Movie, Director
from rest_framework import viewsets
from .serializers import ActorSerializer, MovieSerializer, DirectorSerializer
from django.http.response import JsonResponse
from rest_framework.decorators import api_view
import json

@api_view(['GET', 'POST'])
def get_actor(request):
    if request.method == 'GET':
        getActors = Actor.objects.all()
        serializer = ActorSerializer(getActors, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        create_actor = ActorSerializer(data=request.data)
        if create_actor.is_valid():
            try:
                create_actor.save(name=request.data.get('name'), movieName=request.data.get('movieName'))
                return JsonResponse({'status':'Berhasil tambah data'}, status=201)
            except:
                return JsonResponse({'status':'Gagal'}, status=400)
            

@api_view(['GET'])
def get_movie(request):
    if request.method == 'GET':
        getActors = Movie.objects.all()
        serializer = MovieSerializer(getActors, many=True)
        return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def get_director(request):
    if request.method == 'GET':
        getActors = Director.objects.all()
        serializer = DirectorSerializer(getActors, many=True)
        return JsonResponse(serializer.data, safe=False)

