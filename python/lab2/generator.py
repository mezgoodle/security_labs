from faker import Faker

fake = Faker()


def create_user_data(
    email: str = None,
    first_name: str = None,
    second_name: str = None,
    nickname: str = None,
    password: str = None
):
    return {
        "email": email if email else fake.ascii_company_email(),
        "user_metadata": {},
        "blocked": 'false',
        "email_verified": 'false',
        "app_metadata": {},
        "given_name": first_name if first_name else fake.name(),
        "family_name": second_name if second_name else fake.name(),
        "name": first_name + ' ' + second_name if first_name else fake.name(),
        "nickname": nickname if nickname else fake.name(),
        "verify_email": 'false',
        "picture": "https://i1.wp.com/ssl.gstatic.com/s2/profiles/images/silhouette80.png?ssl=1",
        "connection":"Username-Password-Authentication",
        "password": password if password else fake.name(),
    }
