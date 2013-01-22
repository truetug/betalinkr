# encoding: utf-8
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name=u'Пользователь')

    class Meta:
        verbose_name = u'профиль'
        verbose_name_plural = u'Профили'

    def __unicode__(self):
        return u'для %s' % self.user
