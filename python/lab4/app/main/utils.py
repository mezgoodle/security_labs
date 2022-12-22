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
