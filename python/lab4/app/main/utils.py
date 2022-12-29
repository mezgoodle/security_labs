import requests
from django.conf import settings


def authenticate(username, password):
    response = requests.post(
        f"https://{settings.AUTH0_DOMAIN}/oauth/token",
        data={
            "username": username,
            "password": password,
            "realm": "Username-Password-Authentication",
            "client_id": settings.AUTH0_CLIENT_ID,
            "client_secret": settings.AUTH0_CLIENT_SECRET,
            "audience": settings.AUTH0_API_AUDIENCE,
            "grant_type": "http://auth0.com/oauth/grant-type/password-realm",
            "scope": "offline_access",
        },
    )
    return response.status_code, response.json()


def getUserInfo(token, userId):
    response = requests.get(
        f"https://{settings.AUTH0_DOMAIN}/api/v2/users/{userId}",
        headers={"Authorization": f"Bearer {token}"},
    )
    return response.status_code, response.json()


def refreshToken(token):
    response = requests.post(
        f"https://{settings.AUTH0_DOMAIN}/oauth/token",
        data={
            "grant_type": "refresh_token",
            "client_id": settings.AUTH0_CLIENT_ID,
            "client_secret": settings.AUTH0_CLIENT_SECRET,
            "refresh_token": token,
        },
    )
    return response.status_code, response.json()


def getUserId(email):
    users = usersList()
    for user in users:
        if user["email"] == email:
            return user["user_id"]


def usersList():
    response = requests.get(
        f"https://{settings.AUTH0_DOMAIN}/api/v2/users",
        headers={"Authorization": f"Bearer {settings.API_TOKEN}"},
    )
    return response.json()


def createUser(email, password, name):
    print(settings.API_TOKEN)
    response = requests.post(
        f"https://{settings.AUTH0_DOMAIN}/api/v2/users",
        headers={"Authorization": f"Bearer {settings.API_TOKEN}"},
        data={
            "email": email,
            "user_metadata": {},
            "blocked": "false",
            "email_verified": "false",
            "app_metadata": {},
            "given_name": name,
            "family_name": name,
            "name": name,
            "nickname": "mezgoodle",
            "picture": "config.pictureUrl",
            "connection": "Username-Password-Authentication",
            "password": password,
            "verify_email": "false",
        },
    )
    return response.status_code, response.json()
