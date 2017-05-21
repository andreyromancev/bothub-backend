from rest_framework import views, response, status

from .serializers import AccessTokenSerializer, RefreshTokenSerializer


class AbstractObtainTokenView(views.APIView):
    http_method_names = ('post', 'options')
    serializer_class = None

    def get_serializer_context(self):
        return {
            'request': self.request,
            'view': self,
        }

    def get_serializer(self, *args, **kwargs):
        kwargs['context'] = self.get_serializer_context()
        return self.serializer_class(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            return response.Response(serializer.validated_data)

        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ObtainAccessTokenView(AbstractObtainTokenView):
    serializer_class = AccessTokenSerializer


class ObtainRefreshTokenView(AbstractObtainTokenView):
    serializer_class = RefreshTokenSerializer
