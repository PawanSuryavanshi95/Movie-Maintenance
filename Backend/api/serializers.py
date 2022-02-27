from . models import Movie
from rest_framework import serializers

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=100,)
    desc = serializers.CharField(max_length=200,)
    like = serializers.IntegerField()
    num_actors = serializers.IntegerField()
    release_date = serializers.DateField()

class ActorSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    dob = serializers.DateField()
    num_movies = serializers.IntegerField()

class LinkingSerializer(serializers.Serializer):
    movie_id = serializers.IntegerField()
    actor_id = serializers.IntegerField()