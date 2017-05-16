import random
import hashlib

from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework import serializers, viewsets, status
from rest_framework.response import Response
from rest_framework.validators import UniqueValidator
from rest_framework.decorators import list_route

from bothub.utils.mailer import mail_users


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

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        self._initialize_user(serializer.instance)
        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @list_route(methods=['post'], url_path='activate', serializer_class=ActivateSerializer)
    def activate(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.user
        if user.is_active:
            raise serializers.ValidationError({'detail': 'User is already activated.'})

        user.is_active = True
        user.password = make_password(serializer.validated_data['password'])
        user.save()

        return Response(UserSerializer(user, context={'request': request}).data, status=status.HTTP_202_ACCEPTED)

    def _initialize_user(self, user):
        salt = hashlib.sha1(str(random.random()).encode('utf-8')).hexdigest()[:5]
        activation_key = hashlib.sha1((salt + user.username).encode('utf-8')).hexdigest()

        user.email = user.username
        user.is_active = False
        user.password = activation_key
        user.save()

        mail_users([user.email], 'email_confirm', context={
            'activation_url': '{}/user_activate/?activation_key={}'.format(settings.SITE_WEB, activation_key)
        })
