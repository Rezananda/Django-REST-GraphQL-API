from django.db import models

# Create your models here.

class Actor(models.Model):
    name = models.CharField(max_length=255)
    movieName = models.CharField(max_length=255)

    def __str__(self):
        return str(self.name)

class Movie(models.Model):
    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    year = models.IntegerField()
    actors = models.ManyToManyField(Actor)
    duration = models.CharField(max_length=255)

    def __str__(self):
        return str(self.title)

class Director(models.Model):
    name = models.CharField(max_length=255)
    movies = models.ManyToManyField(Movie)

    def __str__(self):
        return str(self.name)