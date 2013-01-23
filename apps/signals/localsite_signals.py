# encoding: utf-8
from django.contrib.auth.models import User
from django.dispatch.dispatcher import receiver
from django.db.models.signals import post_save

from apps.localsite.models import Profile


@receiver(post_save, sender=User)
def profile_handler(sender, **kwargs):
    instance = kwargs.get('instance')

    try:
        profile = instance.get_profile()
    except Profile.DoesNotExist:
        profile = Profile.objects.create(user=instance)

    return True
