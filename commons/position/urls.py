from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from commons.position import views

urlpatterns = [
    url(r'^get/position/$', views.PositionDetails.as_view(),
        name='refresh-token'),
]