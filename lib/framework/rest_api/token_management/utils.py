import jwt
import uuid
from datetime import datetime
from rest_framework_jwt.settings import api_settings
from rest_framework_jwt.compat import get_username


def refresh_jwt_encode_handler(payload, key):
    return jwt.encode(
        payload,
        key,
        api_settings.JWT_ALGORITHM
    ).decode('utf-8')


def refresh_jwt_decode_handler(token, key):
    return jwt.decode(
        token,
        key,
        api_settings.JWT_VERIFY,
        leeway=api_settings.JWT_LEEWAY,
        audience=api_settings.JWT_AUDIENCE,
        issuer=api_settings.JWT_ISSUER,
        algorithms=[api_settings.JWT_ALGORITHM]
    )


def refresh_jwt_payload_handler(user):
    return {
        'user_id': user.pk,
        'username': get_username(user),
    }


def access_jwt_payload_handler(user):
    payload = {
        'user_id': user.pk,
        'email': user.email,
        'username': get_username(user),
        'exp': datetime.utcnow() + api_settings.JWT_EXPIRATION_DELTA
    }
    if isinstance(user.pk, uuid.UUID):
        payload['user_id'] = str(user.pk)

    if api_settings.JWT_AUDIENCE is not None:
        payload['aud'] = api_settings.JWT_AUDIENCE

    if api_settings.JWT_ISSUER is not None:
        payload['iss'] = api_settings.JWT_ISSUER

    return payload


def get_refresh_secret_key(user):
    return user.password
