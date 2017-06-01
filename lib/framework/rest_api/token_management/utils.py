import jwt
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
        'uid': user.pk,
        'una': get_username(user),
    }


def access_jwt_payload_handler(user):
    return {
        'uid': user.pk,
        'ema': user.email,
        'una': get_username(user),
        'iat': datetime.utcnow(),
        'exp': datetime.utcnow() + api_settings.JWT_EXPIRATION_DELTA,
    }


def get_refresh_secret_key(user):
    return user.password
