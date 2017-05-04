from tastypie.api import Api

from .user import UserResource

api_v1 = Api(api_name='v1')
api_v1.register(UserResource())

