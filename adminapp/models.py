from __future__ import unicode_literals
from django.db import models

# Create your models here.
class User(models.Model):
    user_name=models.CharField(max_length=250)
    email_id = models.EmailField()
    password = models.CharField(max_length=200)
    mobile = models.BigIntegerField()
    dob = models.DateField(auto_now=False,auto_now_add=False)
    leaves = models.IntegerField(default=20)

    def __str__(self):
        return self.user_name