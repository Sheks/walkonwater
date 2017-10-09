# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class FullPermissionsAbstractModel(models.Model):
    class Meta:
        abstract = True
        default_permissions = (
            'add',
            'change',
            'delete',
            'view'
        )


class FeedType(FullPermissionsAbstractModel):
    name = models.CharField(
        max_length=255
    )

    def __str__(self):
        return self.name


class Publisher(FullPermissionsAbstractModel):
    name = models.CharField(
        max_length=500
    )

    def __str__(self):
        return self.name


class Observer(FullPermissionsAbstractModel):
    publisher = models.ForeignKey(
        Publisher
    )
    subscriber = models.ForeignKey(
        User
    )

    def __str__(self):
        return '{} | {}'.format(self.publisher.name, self.subscriber.username)


class Notification(FullPermissionsAbstractModel):
    message = models.CharField(
        max_length=255
    )
    date = models.DateTimeField(
        auto_now_add=True
    )
    owner = models.ForeignKey(
        User
    )
    # type = models.ForeignKey(
    #     FeedType
    # )
    # publisher = models.ForeignKey(
    #     Publisher
    # )

    def __str__(self):
        return '{} | {}'.format(self.message, self.date)

