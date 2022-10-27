from django.shortcuts import render
from .models import Users
from rest_framework.viewsets import ModelViewSet
from .serializers import UsersModelSerializer


class UsersModelViewSet(ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersModelSerializer

# Create your views here.
