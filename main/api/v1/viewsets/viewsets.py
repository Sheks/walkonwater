# -*- coding: utf-8 -*-

from django.contrib.auth.models import User, Group
from rest_framework import viewsets, status, mixins, parsers, renderers, filters, permissions
# from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope


from main.models import Notification
from main.api.v1.serializer import (
    NotificationSerializer,
    UserSerializer,
    GroupSerializer
)


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    # permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    # permission_classes = [permissions.IsAuthenticated]
    required_scopes = ['groups']
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class NotificationViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Notification.objects.all().order_by('id')
    serializer_class = NotificationSerializer
    model = Notification

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
