from django.shortcuts import render

from .utils import authenticate


def index(request):
    if request.method == "POST":
        data = request.POST
        status, data = authenticate(data.get("login"), data.get("password"))
        if status == 200:
            request.session["access_token"] = data["access_token"]
            request.session["refresh_token"] = data["refresh_token"]
    if token := request.session.get("access_token"):
        print(token)
    print(request.session)
    return render(request, "login.html")
