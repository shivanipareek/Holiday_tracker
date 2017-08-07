from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.login_redirect, name='login_redirect'),
    url(r'^login/', include('login.urls')),
    url(r'^leaves/', include('leaves.urls')),
]
