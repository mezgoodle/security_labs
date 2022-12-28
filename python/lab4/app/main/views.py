from django.shortcuts import render, redirect
from django.http import JsonResponse
from authlib.integrations.django_oauth2 import ResourceProtector

from .utils import authenticate, getUserId, getUserInfo, createUser
from . import validator
from .decorators import CustomeResourceProtector

require_auth = CustomeResourceProtector()
validator = validator.Auth0JWTBearerTokenValidator(
    "dev-b34fyn1cot22je3i.us.auth0.com",
    "https://dev-b34fyn1cot22je3i.us.auth0.com/api/v2/",
)
require_auth.register_token_validator(validator)


def index(request):
    user = None
    error = False
    if request.method == "POST":
        data = request.POST
        email = data.get("login")
        status, data = authenticate(email, data.get("password"))
        if status == 200:
            request.session["access_token"] = data["access_token"]
            request.session["refresh_token"] = data["refresh_token"]
            user_id = getUserId(email)
            request.session["user_id"] = user_id
        else:
            error = True
    if access_token := request.session.get("access_token"):
        user_id = request.session["user_id"]
        status, user = getUserInfo(access_token, user_id)
        if status == 200:
            return render(request, "index.html", {"user": user["name"]})
    return render(request, "login.html", {"error": error})


def logout(request):
    request.session["access_token"] = None
    request.session["refresh_token"] = None
    request.session["user_id"] = None
    return redirect("/")


def register(request):
    error = False
    if request.method == "POST":
        data = request.POST
        email = data.get("login")
        password = data.get("password")
        status, data = createUser(email, password, data.get("name"))
        if status == 201:
            _, token_data = authenticate(email, password)
            request.session["access_token"] = token_data["access_token"]
            request.session["refresh_token"] = token_data["refresh_token"]
            request.session["user_id"] = data["user_id"]
            return redirect("/")
        else:
            print(data)
            error = True
    return render(request, "register.html", {"error": error})


def public(request):
    """No access token required to access this route"""
    response = (
        "Hello from a public endpoint! You don't need to be authenticated to see this."
    )
    return JsonResponse(dict(message=response))


@require_auth(None)
def private(request):
    """A valid access token is required to access this route"""
    response = (
        "Hello from a private endpoint! You need to be authenticated to see this."
    )
    return JsonResponse(dict(message=response))
