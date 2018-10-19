from django.conf.urls import url

from dealer.views import view_siebel

urlpatterns = [

    url(r'^sync/dealer/$',
        view_siebel.DealerSyncView.as_view(),
        name='dealer_sync'),
]