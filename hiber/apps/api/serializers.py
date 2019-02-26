from rest_framework import serializers
from django.contrib.auth.models import User
from ..bathouse.models import Bat


class BatSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bat
        fields = ('id', 'common_name', 'scientific_name', 'rarity', 'habits',
                  'size', 'pups', 'risk', 'risk_scope')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'id', 'username')
