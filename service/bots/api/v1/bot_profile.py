from rest_framework import serializers, viewsets

from ...models import BotProfile


class BotProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BotProfile
        fields = ('url', 'id', 'name', 'short_description', 'description')


class BotProfileViewSet(viewsets.ModelViewSet):
    queryset = BotProfile.objects.all()
    serializer_class = BotProfileSerializer
    http_method_names = ('get', 'options')
    search_fields = ('name', 'short_description')

