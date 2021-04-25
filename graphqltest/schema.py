import graphene

from graphene_django.types import DjangoObjectType, ObjectType
from .models import Actor, Movie, Director
import json

class ActorType(DjangoObjectType):
    class Meta:
        model = Actor

class MovieType(DjangoObjectType):
    class Meta:
        model = Movie

class DirectorType(DjangoObjectType):
    class Meta:
        model = Director


class Query(ObjectType):
    actors = graphene.List(ActorType)
    movies = graphene.List(MovieType)
    directors = graphene.List(DirectorType)

    actor = graphene.Field(ActorType, id=graphene.Int())
    movie = graphene.Field(MovieType, id=graphene.Int())
    director = graphene.Field(DirectorType, id=graphene.Int())

    def resolve_actor(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Actor.objects.get(pk=id)
        
        return None

    def resolve_movie(self, info, **kwargs):
        id = kwargs.get('id')
        # year = kwargs.get('year')

        if id is not None:
            return Movie.objects.get(pk=id)
        
        # elif year is not None:
        #     return Movies.objects.get(year=year)
        
        return None

    def resolve_director(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Director.objects.get(pk=id)
        
        return None

    def resolve_actors(self, info, **kwargs):
        print(info.context)
        return Actor.objects.all()

    def resolve_movies(self, info, **kwargs):
        getMovies = Movie.objects.all()
        movies = []
        for movie in getMovies:
            movies.append(movie)
        return movies

    def resolve_directors(self, info,**kwargs):
        getDirector = Director.objects.all()
        directors = []
        for director in getDirector:
            directors.append(director)
        return directors

class CreateActor(graphene.Mutation):
    id = graphene.Int()
    name = graphene.String()
    movieName = graphene.String()

    class Arguments:
        name = graphene.String()
        movieName = graphene.String()

    def mutate(self, info, name, movieName):
        actor = Actor(name=name, movieName=movieName)
        actor.save()

        return CreateActor(
            id = actor.id,
            name = actor.name,
            movieName = actor.movieName
        )

class Mutation(graphene.ObjectType):
    create_actor = CreateActor.Field()

