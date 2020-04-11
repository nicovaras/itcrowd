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

class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'movies_as_actor', 'movies_as_director', 'movies_as_producer', 'aliases']

class MovieSerializer(serializers.HyperlinkedModelSerializer):
    roman_release_year = serializers.SerializerMethodField()
    
    def int_to_roman(self, year):
        ints = (1000, 900,  500, 400, 100,  90, 50,  40, 10,  9,   5,  4,   1)
        nums = ('M',  'CM', 'D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I')
        result = []
        for i in range(len(ints)):
            count = int(year / ints[i])
            result.append(nums[i] * count)
            year -= ints[i] * count
        return ''.join(result)

    def get_roman_release_year(self, obj):
        return "{}".format(self.int_to_roman(obj.release_year))
    class Meta:
        model = Movie
        fields = ['title', 'release_year', 'roman_release_year', 'actors', 'directors', 'producers']

