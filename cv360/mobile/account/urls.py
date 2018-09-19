from django.conf.urls import url


from cv360.mobile.account import views


urlpatterns=[

    url(r'^get/account/bypositionID/$', views.GetAccountByPositionID.as_view(),
        name='get_acc_by_position'),
    ]