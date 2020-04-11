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
	class Meta:
		model = Alias
		fields = ['alias', 'person']

class MovieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Movie
        fields = ['title', 'release_year', 'actors', 'directors', 'producers']

class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name']
