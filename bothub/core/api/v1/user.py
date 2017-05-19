from django.contrib.auth.models import User

from rest_framework import serializers, viewsets, status, permissions
from rest_framework.response import Response
from rest_framework.validators import UniqueValidator
from rest_framework.decorators import list_route


class UserSerializer(serializers.HyperlinkedModelSerializer):
    email = serializers.EmailField(
        required=True, source='username', validators=[UniqueValidator(queryset=User.objects.all())]
    )

    class Meta:
        model = User
        fields = ('email', 'url')


class ActivateSerializer(serializers.Serializer):
    activation_key = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    def __init__(self, *args, **kwargs):
        super(ActivateSerializer, self).__init__(*args, **kwargs)
        self.user = None

    def validate_activation_key(self, value):
        try:
            self.user = User.objects.get(password=value)
        except (User.DoesNotExist, User.MultipleObjectsReturned):
            raise serializers.ValidationError('Wrong activation key.')

        return value


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    http_method_names = ('post', 'get', 'options')
    permission_classes = (permissions.IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        serializer.instance.prepare_for_activation()
        serializer.instance.send_confirmation_email()
        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save(email=self.request.user.username)

    @list_route(methods=['post'], serializer_class=ActivateSerializer)
    def activate(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.user
        if user.is_active:
            raise serializers.ValidationError({'detail': 'User is already activated.'})

        user.activate(serializer.validated_data['password'])

        return Response(UserSerializer(user, context={'request': request}).data, status=status.HTTP_202_ACCEPTED)
