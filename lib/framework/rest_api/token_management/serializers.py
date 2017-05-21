import jwt
from django.contrib.auth import get_user_model, authenticate
from django.utils.translation import ugettext as _
from rest_framework import serializers
from rest_framework_jwt.utils import jwt_encode_handler
from rest_framework_jwt.compat import get_username_field, PasswordField

from .models import RefreshToken
from .settings import TOKEN_DEFAULT_SERVICE
from .utils import (
    refresh_jwt_decode_handler, refresh_jwt_encode_handler, refresh_jwt_payload_handler, get_refresh_secret_key,
    access_jwt_payload_handler
)


class AccessTokenSerializer(serializers.Serializer):
    refresh_token = serializers.CharField(required=True)

    def validate(self, params):
        User = get_user_model()
        refresh_token = params.get('refresh_token')
        refresh_payload = jwt.decode(refresh_token, None, False)
        user_id = refresh_payload.get('user_id')

        try:
            user = User.objects.get(id=user_id, refresh_tokens__key=refresh_token)
        except User.DoesNotExist:
            raise serializers.ValidationError(_('Invalid refresh token.'))

        if not user.is_active:
            msg = _('User account is disabled.')
            raise serializers.ValidationError(msg)

        try:
            refresh_jwt_decode_handler(refresh_token, get_refresh_secret_key(user))
        except jwt.ExpiredSignature:
            raise serializers.ValidationError(_('Signature has expired.'))
        except jwt.DecodeError:
            raise serializers.ValidationError(_('Error decoding signature.'))
        except jwt.InvalidTokenError:
            raise serializers.ValidationError(_('Invalid refresh token.'))

        access_payload = access_jwt_payload_handler(user)
        access_token = jwt_encode_handler(access_payload)

        return {
            'access_token': access_token,
            'refresh_token': refresh_token,
        }


class RefreshTokenSerializer(serializers.Serializer):
    def __init__(self, *args, **kwargs):
        super(RefreshTokenSerializer, self).__init__(*args, **kwargs)

        self.fields[self.username_field] = serializers.CharField()
        self.fields['password'] = PasswordField(write_only=True)

    @property
    def username_field(self):
        return get_username_field()

    def validate(self, params):
        credentials = {
            self.username_field: params.get(self.username_field),
            'password': params.get('password')
        }

        if all(credentials.values()):
            user = authenticate(**credentials)

            if user:
                if not user.is_active:
                    msg = _('User account is disabled.')
                    raise serializers.ValidationError(msg)

                payload = refresh_jwt_payload_handler(user)
                refresh_token = refresh_jwt_encode_handler(payload, get_refresh_secret_key(user))
                refresh_obj, created = RefreshToken.objects.get_or_create(
                    user=user,
                    service=TOKEN_DEFAULT_SERVICE,
                    defaults=dict(
                        key=refresh_token,
                    )
                )
                if not created:
                    refresh_obj.key = refresh_token
                    refresh_obj.save()

                access_payload = access_jwt_payload_handler(user)
                access_token = jwt_encode_handler(access_payload)

                return {
                    'refresh_token': refresh_obj.key,
                    'access_token': access_token,
                }
            else:
                msg = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg)
        else:
            msg = _('Must include "{username_field}" and "password".')
            msg = msg.format(username_field=self.username_field)
            raise serializers.ValidationError(msg)
