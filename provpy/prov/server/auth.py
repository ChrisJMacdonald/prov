from tastypie.authentication import Authentication
from tastypie.authorization import Authorization
from tastypie.authentication import HttpUnauthorized
from tastypie.http import HttpForbidden
from tastypie.exceptions import ImmediateHttpResponse
from django.contrib.auth.models import User
from prov.settings import ANONYMOUS_USER_ID
from models import Container


class AnnonymousAuthentication(Authentication):
    """
    Authenticates only Anonymous users 
    """
    def is_authenticated(self, request, **kwargs):
        if 'HTTP_AUTHORIZATION' in request.META:
            return False
        request.user = User.objects.get(id=ANONYMOUS_USER_ID)
        return True
    
    
class CustomAuthorization(Authorization):
    """
    Authorization of the RESTfull web service
    with object permissions provided by 'django-guardian' package
    """
    
    def methodToPerms(self, method):
        if method == 'GET':
            return 'server.view_container'
        if method == 'POST' or method == 'PUT':
            return 'server.change_container'
        if method == 'DELETE':
            return 'server.delete_container'
        return None
    
    def checkRequest(self, path):
        try:
            if int(path[-2]):
                return True
        except:
            pass
        return False 
    
    def is_authorized(self, request, object=None): #@ReservedAssignment
        path = request.path.split('/');
        if not self.checkRequest(path=path):
            return True
        if request.user.has_perm(self.methodToPerms(request.method), Container.objects.get(id=int(path[-2]))):
            return True
        else:    
            raise ImmediateHttpResponse(HttpForbidden())
    
    def apply_limits(self, request, object_list):
        return filter(lambda obj: request.user.has_perm(self.methodToPerms(request.method),obj), object_list)


"""
Authentication classes imported from tastypie developers version
for compatibility with official one.
"""

class MultiAuthentication(object):
    """
    An authentication backend that tries a number of backends in order.
    """
    def __init__(self, *backends, **kwargs):
        super(MultiAuthentication, self).__init__(**kwargs)
        self.backends = backends

    def is_authenticated(self, request, **kwargs):
        """
        Identifies if the user is authenticated to continue or not.

        Should return either ``True`` if allowed, ``False`` if not or an
        ``HttpResponse`` if you need something custom.
        """
        unauthorized = False

        for backend in self.backends:
            check = backend.is_authenticated(request, **kwargs)

            if check:
                if isinstance(check, HttpUnauthorized):
                    unauthorized = unauthorized or check
                elif check is True:
                    request._authentication_backend = backend
                    return check

        return unauthorized

    def get_identifier(self, request):
        """
        Provides a unique string identifier for the requestor.

        This implementation returns a combination of IP address and hostname.
        """
        try:
            return request._authentication_backend.get_identifier(request)
        except AttributeError:
            return 'nouser'
        

class ApiKeyAuthentication(Authentication):
    """
    Handles API key auth, in which a user provides a username & API key.

    Uses the ``ApiKey`` model that ships with tastypie. If you wish to use
    a different model, override the ``get_key`` method to perform the key check
    as suits your needs.
    """
    def _unauthorized(self):
        return HttpUnauthorized()

    def extract_credentials(self, request):
        if request.META.get('HTTP_AUTHORIZATION') and request.META['HTTP_AUTHORIZATION'].lower().startswith('apikey '):
            (auth_type, data) = request.META['HTTP_AUTHORIZATION'].split()

            if auth_type.lower() != 'apikey':
                raise ValueError("Incorrect authorization header.")

            username, api_key = data.split(':', 1)
        else:
            username = request.GET.get('username') or request.POST.get('username')
            api_key = request.GET.get('api_key') or request.POST.get('api_key')

        return username, api_key

    def is_authenticated(self, request, **kwargs):
        """
        Finds the user and checks their API key.

        Should return either ``True`` if allowed, ``False`` if not or an
        ``HttpResponse`` if you need something custom.
        """
        try:
            username, api_key = self.extract_credentials(request)
        except ValueError:
            return self._unauthorized()

        if not username or not api_key:
            return self._unauthorized()

        try:
            user = User.objects.get(username=username)
        except (User.DoesNotExist, User.MultipleObjectsReturned):
            return self._unauthorized()

#        if not self.check_active(user):
#            return False

        request.user = user
        return self.get_key(user, api_key)

    def get_key(self, user, api_key):
        """
        Attempts to find the API key for the user. Uses ``ApiKey`` by default
        but can be overridden.
        """
        from tastypie.models import ApiKey

        try:
            ApiKey.objects.get(user=user, key=api_key)
        except ApiKey.DoesNotExist:
            return self._unauthorized()

        return True

    def get_identifier(self, request):
        """
        Provides a unique string identifier for the requestor.

        This implementation returns the user's username.
        """
        username, api_key = self.extract_credentials(request)
        return username or 'nouser'
