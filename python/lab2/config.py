import os

config = {
    'kpi': {
        'url_for_token': os.getenv('KPI_URL_FOR_TOKEN', 'https://kpi.eu.auth0.com/oauth/token'),
        'url_for_users': os.getenv('KPI_URL_FOR_USERS', 'https://kpi.eu.auth0.com/api/v2/users'),
        'client_id': os.getenv('KPI_CLIENT_ID', 'JIvCO5c2IBHlAe2patn6l6q5H35qxti0'),
        'client_secret': os.getenv('KPI_CLIENT_SECRET', 'ZRF8Op0tWM36p1_hxXTU-B0K_Gq_-eAVtlrQpY24CasYiDmcXBhNS6IJMNcz1EgB'),
        'audience': os.getenv('KPI_AUDIENCE', 'https://kpi.eu.auth0.com/api/v2/'),
    },
    'myself': {
        'url_for_token': os.getenv('MY_URL_FOR_TOKEN', 'https://dev-b34fyn1cot22je3i.us.auth0.com/oauth/token'),
        'url_for_users': os.getenv('MY_URL_FOR_USERS', 'https://dev-b34fyn1cot22je3i.us.auth0.com/api/v2/users'),
        'client_id': os.getenv('MY_CLIENT_ID', 'C4dFTmHwKV8DXaXkBoCX4RLAoENBsstZ'),
        'client_secret': os.getenv('MY_CLIENT_SECRET', 'Hiuy2N4AdwU-zezmgVKhKHhf-5TINv_82RvwpESbV25ddoUZZ88pRWBXmQVCJ7GB'),
        'audience': os.getenv('MY_AUDIENCE', 'https://dev-b34fyn1cot22je3i.us.auth0.com/api/v2/'),
    }
}
