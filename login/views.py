# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from .serializers import UserProfileSerializer
from .models import UserProfile

