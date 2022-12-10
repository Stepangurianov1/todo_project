from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import MyUsers
from rest_framework.viewsets import ModelViewSet
from .serializers import UsersModelSerializer,UserV2ModelSerializer


class UsersModelViewSet(ModelViewSet):
    queryset = MyUsers.objects.all()
    serializer_class = UsersModelSerializer

    def get_serializer_class(self):
        if self.request.version == 'v1':
            return UsersModelSerializer
        else:
            return UserV2ModelSerializer

        # Create your views here.


class UsersAPIView(APIView):
    def get(self, request, format=None):
        user_id = request.query_params.get('pk')
        users = MyUsers.objects.all()

        if user_id:
            users = MyUsers.objects.filter(id=user_id)
        serializer = UsersModelSerializer(users, many=True)
        return Response(serializer.data)
