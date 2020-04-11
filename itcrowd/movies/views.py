from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from movies.serializers import UserSerializer, GroupSerializer, AliasSerializer, PersonSerializer, MovieSerializer
from movies.models import Movie, Person, Alias
from rest_framework import permissions


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class AliasViewSet(viewsets.ModelViewSet):
    queryset = Alias.objects.all()
    serializer_class = AliasSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer        
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
