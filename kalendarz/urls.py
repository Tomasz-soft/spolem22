from django.conf.urls import url
from django.urls import path, re_path, include
from promocje import views
from towary.views import towary_lista, towary_detail
from sklepy.views import sklepy_lista, sklepy_detail
urlpatterns = [
    url('', include('sklepy.urls')),
    url('', include('promocje.urls')),

    url('', include('towary.urls')),
    url('', include('pracownicy.urls')),
    url('', include('prominfo.urls')),
    url('', include('promcent.urls')),
    url(r'^sklepy/', sklepy_lista),
    url('', include('promczas_cent.urls')),
    url('', include('promczas_info.urls')),
    #url('', include('promczas_sklep.urls')),
]
