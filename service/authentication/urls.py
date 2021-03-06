from django.conf.urls import url, include
from lib.framework.rest_api.token_management.views import ObtainAccessTokenView, ObtainRefreshTokenView

from .api.v1 import urlpatterns as url_v1


urlpatterns = [
    url(r'^api/v1/', include(url_v1)),
    url(r'^api/auth/access_token/', ObtainAccessTokenView.as_view()),
    url(r'^api/auth/refresh_token/', ObtainRefreshTokenView.as_view()),
    url(r'^api/auth/', include('rest_framework.urls')),
]
