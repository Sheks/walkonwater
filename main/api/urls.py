from django.conf.urls import include, url
from rest_framework_nested import routers
from rest_framework.authtoken import views

from main.api.v1.viewsets import (
    NotificationViewSet,
    UserViewSet,
    GroupViewSet
)

router = routers.DefaultRouter()
router.register('notifications', NotificationViewSet)


# Routers provide an easy way of automatically determining the URL conf
auth_router = routers.DefaultRouter()
auth_router.register(r'users', UserViewSet)
auth_router.register(r'groups', GroupViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^', include(auth_router.urls)),
    url(r'^api-token-auth/', views.obtain_auth_token)
    # url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
]

