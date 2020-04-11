from django.contrib.auth.models import User, Group
from rest_framework import serializers
from movies.models import Movie, Person, Alias

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class AliasSerializer(serializers.HyperlinkedModelSerializer):
    class AliasPersonSerializer(serializers.HyperlinkedModelSerializer):
        class Meta:
            model = Person
            fields = ['url' ,'first_name', 'last_name']

    person = AliasPersonSerializer()
    class Meta:
        model = Alias
        fields = ['alias', 'person']

class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class PersonAliasSerializer(serializers.HyperlinkedModelSerializer):
        class Meta:
            model = Alias
            fields = ['url' ,'alias']

    class PersonMovieSerializer(serializers.HyperlinkedModelSerializer):
        class Meta:
            model = Movie
            fields = ['url' ,'title', 'release_year']

    aliases = PersonAliasSerializer(many=True)
    movies_as_actor = PersonMovieSerializer(many=True)
    movies_as_director = PersonMovieSerializer(many=True)
    movies_as_producer = PersonMovieSerializer(many=True)
    
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'movies_as_actor', 'movies_as_director', 'movies_as_producer', 'aliases']

class MovieSerializer(serializers.HyperlinkedModelSerializer):
    class MoviePersonSerializer(serializers.HyperlinkedModelSerializer):
        class Meta:
            model = Person
            fields = ['url' ,'first_name', 'last_name']

    actors = MoviePersonSerializer(many=True)
    directors = MoviePersonSerializer(many=True)
    producers = MoviePersonSerializer(many=True)

    class Meta:
        model = Movie
        fields = ['title', 'release_year', 'actors', 'directors', 'producers']

