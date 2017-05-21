from rest_framework_jwt.authentication import JSONWebTokenAuthentication


class JWTAuthentication(JSONWebTokenAuthentication):
    def authenticate_credentials(self, payload):
        return {
            'id': payload.get('user_id'),
            'username': payload.get('username'),
            'email': payload.get('email'),
        }
