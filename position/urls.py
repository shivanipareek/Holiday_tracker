from position.views import views
from django.conf.urls import url

urlpatterns = [

url(r'^get/position/$', GetPosition.as_view(),
        name='get_position'),
]