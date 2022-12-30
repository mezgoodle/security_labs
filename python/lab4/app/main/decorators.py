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
                        # access_token = request.session["access_token"]
                        access_token = "eyJhbGciOiJSUzI1NiIsInR1cCI6IkpXVCIsImtpZCI6ImppYzdtZHZweTFKMEZrZlA0d1ZQXyJ9.eyJpc3MiOiJodHRwczovL2Rldi1iMzRmeW4xY290MjJqZTNpLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MzkyZjRkZGU0ZTJjMWFmM2ZkMTMyNzEiLCJhdWQiOiJodHRwczovL2Rldi1iMzRmeW4xY290MjJqZTNpLnVzLmF1dGgwLmNvbS9hcGkvdjIvIiwiaWF0IjoxNjcyMzAxNjc3LCJleHAiOjE2NzIzODc2NzcsImF6cCI6IkM0ZEZUbUh3S1Y4RFhhWGtCb0NYNFJMQW9FTkJzc3RaIiwic2NvcGUiOiJyZWFkOmN1cnJlbnRfdXNlciB1cGRhdGU6Y3VycmVudF91c2VyX21ldGFkYXRhIGRlbGV0ZTpjdXJyZW50X3VzZXJfbWV0YWRhdGEgY3JlYXRlOmN1cnJlbnRfdXNlcl9tZXRhZGF0YSBjcmVhdGU6Y3VycmVudF91c2VyX2RldmljZV9jcmVkZW50aWFscyBkZWxldGU6Y3VycmVudF91c2VyX2RldmljZV9jcmVkZW50aWFscyB1cGRhdGU6Y3VycmVudF91c2VyX2lkZW50aXRpZXMgb2ZmbGluZV9hY2Nlc3MiLCJndHkiOiJwYXNzd29yZCJ9.lS2MiKPbsmlVTK-ASExxbuJ5YJothQLibA6JgjI0xke1PwALyhtrJpMux7U-NQPfloOwclV3P7HjLDMP6Xxi7JRIB6hSXo7U--SH861bq9nVunayu7uyFTaJXi0rwMiQ3yHJuZJsTM8Ve7GcqhWn5gyddvtZo-TuOnHVkPjzqCJNYM4t6hK55q-fE1Uao1Uc7JkecWX6CnSEeZjLolQLu4zDVPn28bmAZbdGgJJgqm-zKpxnExalSa5MVNAGPgi9dLscgYYzH7Lt2Bv_J-McKIeKhzmh30YzanajT4ymnCt_ttCF7E9Wcg9wDUl0rBMH6UQAuZ5zxJN6EbkViJhZ6Q"
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
                            {"error": "Your token has been expired or invalid"},
                        )
                return f(request, *args, **kwargs)

            return decorated

        return wrapper
