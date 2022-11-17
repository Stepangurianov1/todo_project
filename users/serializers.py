from .models import Users
from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer


class UsersModelSerializer(ModelSerializer):
    class Meta:
        model = Users
        fields = ('id', 'email', 'first_name', 'last_name', 'username')
