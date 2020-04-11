from django.db import models


class Person(models.Model):
    last_name = models.CharField(max_length=100, blank=False)
    first_name = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class Alias(models.Model):
    alias = models.CharField(max_length=100, blank=False)
    person = models.ForeignKey(
        Person, on_delete=models.CASCADE, related_name='aliases')

    def __str__(self):
        return "{} '{}' {}".format(self.person.first_name, self.alias, self.person.last_name)


class Movie(models.Model):
    title = models.CharField(max_length=100, blank=False)
    release_year = models.IntegerField()
    actors = models.ManyToManyField(Person, related_name='movies_as_actor')
    directors = models.ManyToManyField(
        Person, related_name='movies_as_director')
    producers = models.ManyToManyField(
        Person, related_name='movies_as_producer')

    def __str__(self):
        return "{}".format(self.title)
