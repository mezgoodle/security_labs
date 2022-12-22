from django.shortcuts import render, redirect

from .utils import authenticate, getUserId, getUserInfo


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
        user = getUserInfo(access_token, user_id)
        return render(request, "index.html", {"user": user[1]["name"]})
    return render(request, "login.html", {"error": error})


def logout(request):
    request.session["access_token"] = None
    request.session["refresh_token"] = None
    request.session["user_id"] = None
    return redirect("/")
