from opty.views import views_solr
from django.conf.urls import url


urlpatterns = [
    url(r'^opty/by_pos/$',views_solr.GetOptyByPosAPIView.as_view(),
        name='get_opty_by_pos'),
    url(r'^createopty/$',views_solr.CreateOptyAPIView.as_view(),
        name='create_opty'),


]

