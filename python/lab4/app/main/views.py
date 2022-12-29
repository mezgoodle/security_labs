from django.shortcuts import render, redirect
from django.conf import settings

from .utils import authenticate, getUserId, getUserInfo, createUser
from . import validator
from .decorators import CustomeResourceProtector

require_auth = CustomeResourceProtector()
validator = validator.Auth0JWTBearerTokenValidator(
    settings.AUTH0_DOMAIN,
    settings.AUTH0_API_AUDIENCE,
)
require_auth.register_token_validator(validator)


@require_auth(None)
def index(request):
    user = None
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
            return render(request, "login.html", {"error": "Can't authinticate"})
    access_token = request.session.get("access_token")
    user_id = request.session["user_id"]
    status, user = getUserInfo(access_token, user_id)
    if status == 200:
        return render(request, "index.html", {"user": user["name"]})


def logout(request):
    del request.session["access_token"]
    del request.session["refresh_token"]
    del request.session["user_id"]
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
