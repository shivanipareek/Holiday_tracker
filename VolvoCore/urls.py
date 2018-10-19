from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('opty.urls', namespace='opty')),
    url(r'^api/', include('account.urls', namespace='account')),
    url(r'^api/', include('commons.user_auth.urls', namespace='user_auth')),
    url(r'^api/', include('competitor.urls', namespace='competitor')),
    url(r'^api/', include('dealer.urls', namespace='dealer')),
    ]