import json
from urllib import parse

import requests
from intuitlib.client import AuthClient

from settings import CLIENT_ID, CLIENT_SECRET, ENVIRONMENT, REDIRECT_URI, SCOPES, PRODUCTION_URL


class QBO:
    def __init__(self,
                 client_id=CLIENT_ID,
                 client_secret=CLIENT_SECRET,
                 redirect_uri=REDIRECT_URI,
                 env=ENVIRONMENT,
                 scopes=SCOPES):

        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        self.env = env
        self.scopes = scopes

        self._setup()

    def _setup(self):
        self.session = AuthClient(
            self.client_id,
            self.client_secret,
            self.redirect_uri,
            self.env
        )

        self.handle_callback_url()
        self.get_bearer_token()

    def handle_callback_url(self):
        auth_url = self.session.get_authorization_url(scopes=self.scopes)
        print(f"Auth URL: {auth_url}")
        callback_url = input('Paste AUTH_URL in your browser and Copy/Paste the new URL here:')

        query = parse.urlparse(callback_url).query
        params = parse.parse_qs(query)

        self.auth_code = params['code'][0]
        self.state = params['state'][0]
        self.realm_id = params['realmId'][0]

    def get_bearer_token(self):
        return self.session.get_bearer_token(self.auth_code, realm_id=self.realm_id)

    def read(self, object_type, object_id):
        url = f"{PRODUCTION_URL}/v3/company/{self.realm_id}/{object_type}/{object_id}?minorversion=57"
        headers = {
            "Accept": "application/json",
            "Authorization": "Bearer " + self.session.access_token,
            "Content-Type": "application/json"
        }
        resp = requests.request("GET", url, headers=headers)

        if resp.status_code == 200:
            return json.dumps(resp.json(), indent=4)
        else:
            resp = f"The script couldn't read the #{object_id} {str(object_type).capitalize()} object."
            return resp
