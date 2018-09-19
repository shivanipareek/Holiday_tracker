# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.utils import timezone
from django_mysql.models import ListCharField
from enum import Enum
from jsonfield import JSONField
from oauth2_provider.models import AccessToken


class UserDeviceInformation(models.Model):
    user = models.ForeignKey(User)
    device = models.CharField(max_length=80, null=True)
    app_version = models.CharField(max_length=80, null=True)
    access_token = models.CharField(max_length=80, null=True)
    refresh_token = models.CharField(max_length=80, null=True)
    app_name = models.CharField(max_length=80, null=True)
    db_version = models.CharField(max_length=20, null=True)

    class Meta:
        db_table = 'user_device_information'


class Language(Enum):
    EN = 'English'
    ES = 'Spanish'

    @classmethod
    def as_tuple(cls):
        return ((item.value, item.name.replace('_', ' ')) for item in cls)


class UserDetailInformation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_position_details = JSONField(null=True)
    last_login = models.DateTimeField(default=timezone.now())
    last_notification_date = models.DateTimeField(default=timezone.now())
    language = models.CharField(null=True, max_length=20,
                                choices=Language.as_tuple(), default="EN")
    favourite_contacts = models.CharField(null=True, blank=True,
                                          max_length=255)
    favourite_accounts = models.CharField(null=True, blank=True,
                                          max_length=255)
    favourite_opty = ListCharField(
        base_field=models.CharField(max_length=10, default=[]),
        size=6,
        max_length=(6 * 11), null=True, blank=True
    )
    favourite_lead = ListCharField(
        base_field=models.CharField(max_length=10, default=[]),
        size=6,
        max_length=(6 * 11), null=True, blank=True
    )
    user_account = ListCharField(
        base_field=models.CharField(max_length=10, default=[]),
        size=6,
        max_length=(6 * 11), null=True, blank=True
    )

    logged_in_pos_id = models.CharField(null=True, blank=True, max_length=255)

    class Meta:
        db_table = 'user_detail'


def record_login(sender, instance, *args, **kwargs):
    try:
        user = UserDetailInformation.objects.filter(user=instance.user)
        user = user[0]
        user.last_login = timezone.now()
        user.save()

    except Exception, e:
        print e
        pass


post_save.connect(record_login, sender=AccessToken)


class UserPositionDeviceDetails(models.Model):
    user = models.ForeignKey(User)
    position_id = models.CharField(null=True, blank=True, max_length=50)
    device_id = models.CharField(null=True, blank=True, max_length=100)
    username = models.CharField(null=True, blank=True, max_length=100)
    position_type = models.CharField(null=True, blank=True, max_length=100)
    first_name = models.CharField(null=True, blank=True, max_length=100)
    last_name = models.CharField(null=True, blank=True, max_length=100)
    sr_list = ListCharField(
        base_field=models.CharField(max_length=10, default=[]),
        size=6,
        max_length=(6 * 11), null=True, blank=True
    )
    position_accounts = ListCharField(
        base_field=models.CharField(max_length=10, default=[]),
        size=6,
        max_length=(6 * 11), null=True, blank=True
    )
    sr_account = ListCharField(
        base_field=models.CharField(max_length=10, default=[]),
        size=6,
        max_length=(6 * 11), null=True, blank=True
    )
    sr_position_details = JSONField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    is_active = models.BooleanField(default=True)
