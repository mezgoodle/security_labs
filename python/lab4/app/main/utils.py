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


def refreshToken(token):
    response = requests.post(
        f"https://dev-b34fyn1cot22je3i.us.auth0.com/oauth/token",
        data={
            "grant_type": "refresh_token",
            "client_id": "C4dFTmHwKV8DXaXkBoCX4RLAoENBsstZ",
            "client_secret": "Hiuy2N4AdwU-zezmgVKhKHhf-5TINv_82RvwpESbV25ddoUZZ88pRWBXmQVCJ7GB",
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
        "https://dev-b34fyn1cot22je3i.us.auth0.com/api/v2/users",
        headers={
            "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImppYzdtZHZweTFKMEZrZlA0d1ZQXyJ9.eyJpc3MiOiJodHRwczovL2Rldi1iMzRmeW4xY290MjJqZTNpLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJDNGRGVG1Id0tWOERYYVhrQm9DWDRSTEFvRU5Cc3N0WkBjbGllbnRzIiwiYXVkIjoiaHR0cHM6Ly9kZXYtYjM0ZnluMWNvdDIyamUzaS51cy5hdXRoMC5jb20vYXBpL3YyLyIsImlhdCI6MTY3MjIxOTI1NCwiZXhwIjoxNjcyMzA1MjU0LCJhenAiOiJDNGRGVG1Id0tWOERYYVhrQm9DWDRSTEFvRU5Cc3N0WiIsInNjb3BlIjoicmVhZDp1c2VycyB1cGRhdGU6dXNlcnMgY3JlYXRlOnVzZXJzIiwiZ3R5IjoiY2xpZW50LWNyZWRlbnRpYWxzIn0.bb1-ew8uACIL9WK0f0QjXg_pomgEz-CAyMXpUqlJpX1wXpkhx4xl8OoF61gn6WF6Xk-NIgW5AR2kgzGDVnujHvEII2LxexK8ptJj195hSbwbY-My3zrrWIJFw25ZE2P-WDGULMie-O7Ib688eNjIi6hWWVpobXnfs6hqgGykVG-9bLqS_YD2AvUIGWhOYdM2PEleYvPYM_A5lChXd3zg7Fh0qXzaqR8HobMAHewAgckA1ij4hA7zClrm5WER-x_PF0zH1hRWTG8N_pVeeVC62xM6t_UK5NTAKATs5I0Q_HQdMp7EGlff031nRgK0hnoHluIEwXL1FvUSlhBt2DlPLQ"
        },
    )
    return response.json()


def createUser(email, password, name):
    response = requests.post(
        "https://dev-b34fyn1cot22je3i.us.auth0.com/api/v2/users",
        headers={
            "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImppYzdtZHZweTFKMEZrZlA0d1ZQXyJ9.eyJpc3MiOiJodHRwczovL2Rldi1iMzRmeW4xY290MjJqZTNpLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJDNGRGVG1Id0tWOERYYVhrQm9DWDRSTEFvRU5Cc3N0WkBjbGllbnRzIiwiYXVkIjoiaHR0cHM6Ly9kZXYtYjM0ZnluMWNvdDIyamUzaS51cy5hdXRoMC5jb20vYXBpL3YyLyIsImlhdCI6MTY3MjIxOTI1NCwiZXhwIjoxNjcyMzA1MjU0LCJhenAiOiJDNGRGVG1Id0tWOERYYVhrQm9DWDRSTEFvRU5Cc3N0WiIsInNjb3BlIjoicmVhZDp1c2VycyB1cGRhdGU6dXNlcnMgY3JlYXRlOnVzZXJzIiwiZ3R5IjoiY2xpZW50LWNyZWRlbnRpYWxzIn0.bb1-ew8uACIL9WK0f0QjXg_pomgEz-CAyMXpUqlJpX1wXpkhx4xl8OoF61gn6WF6Xk-NIgW5AR2kgzGDVnujHvEII2LxexK8ptJj195hSbwbY-My3zrrWIJFw25ZE2P-WDGULMie-O7Ib688eNjIi6hWWVpobXnfs6hqgGykVG-9bLqS_YD2AvUIGWhOYdM2PEleYvPYM_A5lChXd3zg7Fh0qXzaqR8HobMAHewAgckA1ij4hA7zClrm5WER-x_PF0zH1hRWTG8N_pVeeVC62xM6t_UK5NTAKATs5I0Q_HQdMp7EGlff031nRgK0hnoHluIEwXL1FvUSlhBt2DlPLQ"
        },
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
