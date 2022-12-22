import requests


def authenticate(username, password):
    response = requests.post(
        "https://dev-b34fyn1cot22je3i.us.auth0.com/oauth/token",
        data={
            "username": username,
            "password": password,
            "realm": "Username-Password-Authentication",
            "client_id": "C4dFTmHwKV8DXaXkBoCX4RLAoENBsstZ",
            "client_secret": "Hiuy2N4AdwU-zezmgVKhKHhf-5TINv_82RvwpESbV25ddoUZZ88pRWBXmQVCJ7GB",
            "audience": "https://dev-b34fyn1cot22je3i.us.auth0.com/api/v2/",
            "grant_type": "http://auth0.com/oauth/grant-type/password-realm",
            "scope": "offline_access",
        },
    )
    return response.status_code, response.json()


def getUserInfo(token, userId):
    response = requests.get(
        f"https://dev-b34fyn1cot22je3i.us.auth0.com/api/v2/users/{userId}",
        headers={"Authorization": f"Bearer {token}"},
    )
    return response.status_code, response.json()


def getUserId(email):
    users = usersList()
    for user in users:
        if user["email"] == email:
            return user["user_id"]


def usersList():
    response = requests.get(
        "https://dev-b34fyn1cot22je3i.us.auth0.com/api/v2/users",
        headers={
            "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImppYzdtZHZweTFKMEZrZlA0d1ZQXyJ9.eyJpc3MiOiJodHRwczovL2Rldi1iMzRmeW4xY290MjJqZTNpLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJDNGRGVG1Id0tWOERYYVhrQm9DWDRSTEFvRU5Cc3N0WkBjbGllbnRzIiwiYXVkIjoiaHR0cHM6Ly9kZXYtYjM0ZnluMWNvdDIyamUzaS51cy5hdXRoMC5jb20vYXBpL3YyLyIsImlhdCI6MTY3MTcxOTMxMSwiZXhwIjoxNjcxODA1NzExLCJhenAiOiJDNGRGVG1Id0tWOERYYVhrQm9DWDRSTEFvRU5Cc3N0WiIsInNjb3BlIjoicmVhZDp1c2VycyB1cGRhdGU6dXNlcnMgY3JlYXRlOnVzZXJzIHVwZGF0ZTp1c2Vyc19hcHBfbWV0YWRhdGEiLCJndHkiOiJjbGllbnQtY3JlZGVudGlhbHMifQ.KBY-ox6UxDyVJqMQ8qMji2hhuRPKRGejpum9yeAXC2fkPlcslZcQFejQ5ydy8QtHoBqjiNsOUTYLWOirh9008EDiIvTXm6OfxdjOB9mm8NpiCzkXKJqGLsgM0vYqj02qXUE6r_3dsmEU0XmcHt4kfWI_H-Tzu_gsjItsUkhQtdsD97_XZBHUvXRUGBo6V94Sz-KxMKtDBHCAw92ZCkzivk1QakU5VVHBOgRMFWP-a0MIqY18KD1ctthTOY03Q2JN6Qkdn6mX1-L62d3Kz7e6tUDM-RR-pPiOh7TFV8jQJhJrd8WbRCRt_P1B4ADsNbst_Y2qeEpPLMoGFhZywhXHVQ"
        },
    )
    return response.json()
