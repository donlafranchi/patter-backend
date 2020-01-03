from django.contrib.auth.models import User
from rest_framework import serializers

from general.models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('__all__')


class VenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venue
        fields = ('__all__')


class EventSerializer(serializers.ModelSerializer):
    background = serializers.SerializerMethodField('get_background')

    class Meta:
        model = Event
        fields = ('__all__')

    def get_background(self, obj):
        return obj.background.url if obj.background else ''
