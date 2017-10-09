
from django.contrib import admin

from main.models import (
    Notification,
    FeedType,
    Publisher,
    Observer
)
# Register your models here.


class FeedAdmin(admin.ModelAdmin):
    pass


class FeedTypeAdmin(admin.ModelAdmin):
    pass


class PublisherAdmin(admin.ModelAdmin):
    pass


class ObserverAdmin(admin.ModelAdmin):
    pass


# admin.site.register(FeedType, FeedTypeAdmin)
# admin.site.register(Publisher, PublisherAdmin)
# admin.site.register(Observer, ObserverAdmin)
admin.site.register(Notification, FeedAdmin)
