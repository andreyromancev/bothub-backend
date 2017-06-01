from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^', include('service.authentication.urls')),
    url(r'^', include('service.interaction.urls')),
    url(r'^', include('service.market.urls')),
]
