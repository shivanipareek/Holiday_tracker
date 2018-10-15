from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from Opty import views

urlpatterns = [
    url(r'', views.OptyDetails.as_view(),
        name='Opty_details')
    ]