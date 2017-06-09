from django.conf.urls import url, include

from .api.v1 import urlpatterns as url_v1


urlpatterns = [
    url(r'^api/v1/', include(url_v1)),
]
