from django.conf.urls import include, url
from . import views
from django.contrib.auth.views import login
from rest_framework.urlpatterns import format_suffix_patterns


app_name = 'login'

urlpatterns = [
    url(r'^$', login, {'template_name':'login/login.html'},name='log'),
]

urlpatterns = format_suffix_patterns(urlpatterns)