from django.contrib.auth.models import User
from rest_framework import authentication
from rest_framework import exceptions
from questions.models import Tenant
from django.core.exceptions import ValidationError
class TenantAuthentication  (authentication.BaseAuthentication):

    def authenticate(self, request):
        user = None
        if 'key' in request.GET:
            key = request.GET['key']
            try:
                tenant = Tenant.objects.get(key=key)
                user = tenant.user
            except Tenant.DoesNotExist:
                raise exceptions.AuthenticationFailed('Oops, Key is invalid.')
            except ValidationError:
                raise exceptions.AuthenticationFailed('Oops, Key is invalid.')
        else:
            raise exceptions.AuthenticationFailed('Oops, Key is missing or invalid.')
        return (user, None)