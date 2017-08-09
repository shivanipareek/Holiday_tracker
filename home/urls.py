from django.conf.urls import include, url
from . import views

app_name = 'home'

urlpatterns = [
    url(r'^$', views.Homeview.as_view(), name='home'),
]
