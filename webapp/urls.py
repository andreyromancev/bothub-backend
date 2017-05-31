from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^', include('service.auth_bothub.urls')),
    url(r'^', include('service.interaction.urls')),
    url(r'^', include('service.market.urls')),
]
