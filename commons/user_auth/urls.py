from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from commons.user_auth.views import AddSolrUserView

urlpatterns = [
    url(r'^add/user/$',
        AddSolrUserView.as_view(),
        name='add_solr_user'),

]

urlpatterns = format_suffix_patterns(urlpatterns)
