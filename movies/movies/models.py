from django.db import models

class Person(models.Model):
    last_name = models.CharField(max_length=100, blank=False)
    first_name = models.CharField(max_length=100, blank=False)
    aliases = models.TextField()
    movies_as_actor
    movies_as_director
    movies_as_producer

class Movie(models.Model):
    title = models.CharField(max_length=100, blank=False)
    release_year = models.IntegerField()
    casting
    directors
    producers




