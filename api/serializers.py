from django.contrib.auth.models import User, Group
from api.models import Local
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class LocalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Local
        fields = ('id', 'nombre', 'url', 'direccion', 'cuit')
