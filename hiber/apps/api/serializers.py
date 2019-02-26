from django.contrib.auth.models import User
from drf_extra_fields.fields import FloatRangeField, IntegerRangeField
from rest_framework import serializers
from wagtail.images.api.fields import ImageRenditionField
from ..bathouse.models import Bat


class BatSerializer(serializers.HyperlinkedModelSerializer):
    # TODO: Get base image exposed over API as well
    #       Get current image to display an absolute path over API
    rarity = serializers.CharField(source='get_rarity_display')
    habits = serializers.ListField(source='get_habits_display')
    size = FloatRangeField()
    pups = IntegerRangeField()
    risk = serializers.ListField(source='get_risk_display')
    risk_scope = serializers.ListField(source='get_risk_scope_display')
    bat_image = ImageRenditionField('fill-200x200')

    class Meta:
        model = Bat
        fields = ('id', 'common_name', 'scientific_name', 'rarity', 'habits',
                  'size', 'pups', 'risk', 'risk_scope', 'bat_image')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'id', 'username')
