from aiohttp import ClientSession
import asyncio

from typing import Tuple
from datetime import datetime, timedelta
import platform
from pprint import pprint

from generator import create_user_data


if platform.system()=='Windows':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


class API:
    def __init__(self) -> None:
        self.session = ClientSession()

    async def get(self, url: str, headers: dict = None) -> dict:
        async with self.session.get(url, headers=headers) as response:
            return await response.json()

    async def post(self, url: str, data: dict = None, headers: dict = None) -> Tuple[dict, int]:
        async with self.session.post(url, data=data, headers=headers) as response:
            return await response.json(), response.status


async def work_with_api(
    url_for_token: str,
    url_for_users: str,
    client_id: str,
    client_secret: str,
    audience: str,
    grant_type: str = 'client_credentials'
):
    api = API()

    token_data, status = await api.post(url_for_token, {
        'client_id': client_id,
        'client_secret': client_secret,
        'audience': audience,
        'grant_type': grant_type
    })
    assert status == 200
    current_time = datetime.now()
    print(f'Getting token {token_data["access_token"]}, expires in {current_time + timedelta(seconds=token_data["expires_in"])}')

    data, status = await api.post(
        url_for_users,
        create_user_data(
            'mezgoodle@gmail.com',
            'Maksym',
            'Zavalniuk',
            'mezgoodle',
            'ftl4Guc4!D32'
        ),
        {'Authorization': f'{token_data["token_type"]} {token_data["access_token"]}'}
    )
    assert status == 201
    print(f'User with id {data["user_id"]} has been created')

    data = await api.get(
        f'{url_for_users}/{data["user_id"]}',
        {'Authorization': f'{token_data["token_type"]} {token_data["access_token"]}'}
    )
    pprint(data)


async def main():
    await work_with_api(
        'https://kpi.eu.auth0.com/oauth/token',
        'https://kpi.eu.auth0.com/api/v2/users',
        'JIvCO5c2IBHlAe2patn6l6q5H35qxti0',
        'ZRF8Op0tWM36p1_hxXTU-B0K_Gq_-eAVtlrQpY24CasYiDmcXBhNS6IJMNcz1EgB',
        'https://kpi.eu.auth0.com/api/v2/'
    )
    await work_with_api(
        'https://dev-b34fyn1cot22je3i.us.auth0.com/oauth/token',
        'https://dev-b34fyn1cot22je3i.us.auth0.com/api/v2/users',
        'C4dFTmHwKV8DXaXkBoCX4RLAoENBsstZ',
        'Hiuy2N4AdwU-zezmgVKhKHhf-5TINv_82RvwpESbV25ddoUZZ88pRWBXmQVCJ7GB',
        'https://dev-b34fyn1cot22je3i.us.auth0.com/api/v2/'
    )


asyncio.run(main())
