# encoding: utf-8
from django.contrib import admin

from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user',)
    list_filter = ()
    readonly_fields = ('user',)

admin.site.register(Profile, ProfileAdmin)
