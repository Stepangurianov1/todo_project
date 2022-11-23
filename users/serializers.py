from .models import MyUsers
from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer


class UsersModelSerializer(ModelSerializer):
    class Meta:
        model = MyUsers
        fields = ('id', 'email', 'first_name', 'last_name', 'username')
