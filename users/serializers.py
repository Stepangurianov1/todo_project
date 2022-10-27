from .models import Users
from rest_framework.serializers import HyperlinkedModelSerializer


class UsersModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Users
        fields = ('email', 'first_name', 'last_name', 'username')
