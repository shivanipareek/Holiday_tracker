from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Leave(models.Model):
    from_date = models.DateField(auto_now= False,auto_now_add=False)
    upto_date = models.DateField(auto_now=False, auto_now_add=False)
    calculated_leaves = models.IntegerField()
    reason = models.CharField(max_length=2000)