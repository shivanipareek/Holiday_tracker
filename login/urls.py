from django.conf.urls import include, url
from . import views
from django.contrib.auth.views import login

urlpatterns = [
    url(r'^$', login, {'template_name':'login/login.html'}),
]