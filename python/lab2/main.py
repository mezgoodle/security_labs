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


async def main():
    api = API()
    token_data, status = await api.post('https://kpi.eu.auth0.com/oauth/token', {
        'client_id': 'JIvCO5c2IBHlAe2patn6l6q5H35qxti0',
        'client_secret': 'ZRF8Op0tWM36p1_hxXTU-B0K_Gq_-eAVtlrQpY24CasYiDmcXBhNS6IJMNcz1EgB',
        'audience': 'https://kpi.eu.auth0.com/api/v2/',
        'grant_type': 'client_credentials'
    })
    assert status == 200
    current_time = datetime.now()
    print(f'Getting token {token_data["access_token"][:5]}..., expires in {current_time + timedelta(seconds=token_data["expires_in"])}')
    data, status = await api.post(
        'https://kpi.eu.auth0.com/api/v2/users',
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
        f'https://kpi.eu.auth0.com/api/v2/users/{data["user_id"]}',
        {'Authorization': f'{token_data["token_type"]} {token_data["access_token"]}'}
    )
    pprint(data)


asyncio.run(main())
