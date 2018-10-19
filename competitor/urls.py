from competitor.views import views_solr
from django.conf.urls import url

urlpatterns =[

    url(r'^competitor/byoptyId/$',views_solr.GetCompetitorByOptyIDAPIView.as_view(),
        name='get_competitor_byoptyID'),
    ]