from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Users
from rest_framework.viewsets import ModelViewSet
from .serializers import UsersModelSerializer


class UsersModelViewSet(ModelViewSet):
    queryset = Users.objects.all()
    user = Users.objects.get(id=1)
    print(user.id)
    serializer_class = UsersModelSerializer


# Create your views here.

class UsersAPIView(APIView):
    def get(self, request, format=None):
        user_id = request.query_params.get('pk')
        users = Users.objects.all()

        if user_id:
            users = Users.objects.filter(id=user_id)
        serializer = UsersModelSerializer(users, many=True)
        return Response(serializer.data)
