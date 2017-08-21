from django.conf.urls import include, url
from . import views
from django.contrib.auth.decorators import login_required
from rest_framework.urlpatterns import format_suffix_patterns
app_name = 'home'

urlpatterns = [
    url(r'^$', login_required(views.Homeview.as_view(template_name="home/home.html")),name='home'),
]

urlpatterns = format_suffix_patterns(urlpatterns)