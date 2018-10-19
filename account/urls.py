from account.views import views_solr
from django.conf.urls import url

urlpatterns = [

    url(r'^acc/by_pos/$',
        views_solr.GetAccByPosAPIView.as_view(),
        name='get_acc_by_pos'),


]

