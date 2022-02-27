from django.http import JsonResponse
from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

from django.views.decorators.csrf import csrf_exempt

from .serializers import ActorSerializer, MovieSerializer
from .models import Actor, Linking, Movie

def ShowAll(request, sort):
    if request.method=='GET':
        print(sort)
        movies = Movie.objects.all().order_by(sort)
        for i in range(len(movies)):
            actors = Linking.objects.filter(movie_id=movies[i].id)
            movies[i].num_actors = len(actors)
        serializer = MovieSerializer(movies, many=True)
        return JsonResponse(serializer.data, safe=False)
    else:
        return JsonResponse({'success':False, 'message':'Wrong Request'})

def ShowAllActors(request):
    if request.method=='GET':
        actors = Actor.objects.all()
        for i in range(len(actors)):
            movies = Linking.objects.filter(actor_id=actors[i].id)
            actors[i].num_movies = len(movies)
        serializer = ActorSerializer(actors, many=True)
        return JsonResponse(serializer.data, safe=False)
    else:
        return JsonResponse({'success':False, 'message':'Wrong Request'})

@csrf_exempt
def updateMovie(request):
    if request.method=='POST':
        jsonData = JSONParser().parse(request)
        print(jsonData)
        movie = Movie.objects.get(id=jsonData['id'])
        movie.like = movie.like +  jsonData['like']
        movie.save()
        return JsonResponse({'success':True});

    else:
        return JsonResponse({'success':False, 'message':'Wrong Request'})
