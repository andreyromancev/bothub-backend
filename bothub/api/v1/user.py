from django.contrib.auth.models import User
from django.conf.urls import url
from tastypie.resources import ModelResource
from tastypie.http import HttpAccepted


class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        allowed_methods = []
