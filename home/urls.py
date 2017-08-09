from django.conf.urls import include, url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
app_name = 'home'

urlpatterns = [
    url(r'^$', views.Homeview.as_view(), name='home'),
]

urlpatterns = format_suffix_patterns(urlpatterns)