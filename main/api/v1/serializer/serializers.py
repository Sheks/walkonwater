# -*- coding: utf-8 -*-

from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework_json_api import serializers as json_serializers
from rest_framework_json_api.relations import ResourceRelatedField

from main.models import Notification


class UserSerializer(json_serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class GroupSerializer(json_serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('name', )


class NotificationSerializer(
    json_serializers.HyperlinkedModelSerializer
):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Notification
        fields = ('id', 'message', 'date')
