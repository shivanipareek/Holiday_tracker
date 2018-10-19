from __future__ import unicode_literals
from django.db import models

class Opty(models.Model):
    """
    Base class for storing Siebel Opty ID and Opty ID.
    """
    opty_id = models.CharField(max_length=200, blank=False)
    seibel_opty_id = models.CharField(max_length=200, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'Opty'

