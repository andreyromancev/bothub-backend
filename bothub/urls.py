from django.conf.urls import url, include
from django.contrib import admin

from .api import api_v1


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(api_v1.urls)),
]
