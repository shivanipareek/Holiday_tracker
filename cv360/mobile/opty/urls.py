from django.conf.urls import url
from cv360.mobile.opty import views

urlpatterns = [

    url(r'^get/opty/bypos/$', views.GetOptyByPosition.as_view(),
        name='get_opty_by_position'),
    url(r'^createopty/$', views.Createopty.as_view(),
        name='create_opty'),
]