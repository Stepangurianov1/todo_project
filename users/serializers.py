from .models import MyUsers
from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer


class UsersModelSerializer(ModelSerializer):
    class Meta:
        model = MyUsers
        fields = ('id', 'email', 'first_name', 'last_name', 'username')


class UserV2ModelSerializer(ModelSerializer):
    class Meta:
        model = MyUsers
        fields = ('is_active', 'is_superuser')
