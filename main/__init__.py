from django.db.models.signals import post_migrate
from django.dispatch import receiver


@receiver(post_migrate)
def add_user_and_group_view_permissions(sender, **kwargs):
    from django.contrib.auth.models import Permission
    from django.contrib.contenttypes.models import ContentType
    content_type = ContentType.objects.get(app_label='auth', model='user')
    Permission.objects.get_or_create(codename='view_user', name='Can View User', content_type=content_type)
    content_type = ContentType.objects.get(app_label='auth', model='group')
    Permission.objects.get_or_create(codename='view_group', name='Can View Group', content_type=content_type)
