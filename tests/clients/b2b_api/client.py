import json
import os
from json import JSONEncoder

import requests
from keycloak import Keycloak


class YandehClient(object):

    def __init__(self, base_url, client_id):
        self.base_url = base_url
        self.client_id = client_id
        self.it_client_id = os.environ.get('YANDEH_IT_CLIENT_ID', 'yandeh-integration-test')
        self.it_client_secret = os.environ.get('YANDEH_IT_CLIENT_SECRET')
        if not self.client_secret:
            raise ValueError('SSO client secret not provided')

        realm = self.keycloak_base_url.split('/')[-1]
        keycloak_base = self.keycloak_base_url.replace(
            f'/auth/realms/{realm}', '')
        keycloak_base_url = os.environ.get(
            'KEYCLOAK_BASE_URL',
            'https://sso-dev.yandeh.com.br/auth/realms/YandehQA'
        )
        print(keycloak_base_url)
        self.sso = Keycloak(
            keycloak_base, realm,
            client_id=self.it_client_id,
            client_secret=self.it_client_secret
        )

    def _req(self, method, resource, body=None, params=None):
        url = f'{self.base_url}/{resource}'
        headers = {
            'Authorization': f'Bearer {self.sso.exchange_token(self.client_id)}'
        }
        if method in ['POST', 'PUT']:
            headers['Content-Type'] = 'application/json'
        resp = requests.request(
            method, url, headers=headers, data=json.dumps(body, cls=JSONEncoder), params=params)
        resp.raise_for_status()
        return resp


class B2BApiClient(YandehClient):

    def __init__(self):
        base_url = os.environ(
            'B2B_API_BASE_URL',
            'https://b2b-api-staging.devyandeh.com.br'
        )
        super().__init__(base_url, 'b2b-api')
        self.campaign_resource = '/offers'

    def create_campaign(self, campaign):
        self._req('POST', self.campaign_resource, body={})

    def create_goals_campaign(self):
        campaign = {
            'offer_type': 'GOAL_ACHIEVEMENTS'
        }
        self.create_campaign(campaign)
