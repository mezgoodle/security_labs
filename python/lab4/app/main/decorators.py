import functools
from django.shortcuts import render
from authlib.oauth2 import (
    OAuth2Error,
    ResourceProtector as _ResourceProtector,
)
from authlib.oauth2.rfc6749 import (
    MissingAuthorizationError,
    HttpRequest,
)
from authlib.oauth2.rfc6750 import BearerTokenValidator as _BearerTokenValidator


class CustomeResourceProtector(_ResourceProtector):
    def acquire_token(self, request, scopes=None, add_header: dict = None):
        """A method to acquire current valid token with the given scope.

        :param request: Django HTTP request instance
        :param scopes: a list of scope values
        :return: token object
        """
        url = request.build_absolute_uri()
        headers = dict(request.headers)
        headers.update(add_header)
        req = HttpRequest(
            request.method,
            url,
            None,
            headers,
        )
        req.req = request
        if isinstance(scopes, str):
            scopes = [scopes]
        token = self.validate_request(scopes, req)
        return token

    def __call__(self, scopes=None, optional=False):
        def wrapper(f):
            @functools.wraps(f)
            def decorated(request, *args, **kwargs):
                if request.method != "POST":
                    add_header = {}
                    try:
                        access_token = request.session["access_token"]
                        add_header = {"Authorization": f"Bearer {access_token}"}
                    except KeyError:
                        pass
                    try:
                        token = self.acquire_token(request, scopes, add_header)
                        request.oauth_token = token
                    except MissingAuthorizationError:
                        if optional:
                            request.oauth_token = None
                            return f(request, *args, **kwargs)
                        return render(
                            request, "login.html", {"error": "You need to log in"}
                        )
                    except OAuth2Error:
                        return render(
                            request,
                            "login.html",
                            {"error": "Your token has been expired"},
                        )
                return f(request, *args, **kwargs)

            return decorated

        return wrapper
