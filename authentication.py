import random
import string
from requests_oauthlib.oauth2_session import OAuth2Session

__author__ = 'julio'

client_id = '3793319835.3795254942'
client_secret = 'd221a0dd82b0d47205f1abac0f1a5257'
authorize_url = 'https://slack.com/oauth/authorize'
token_url = 'https://slack.com/api/oauth.access'

class Authentication:
    state = ''

    def login(self):
        slack = OAuth2Session(client_id)
        authorization_url, state = slack.authorization_url(authorize_url)

        self.state = state

        return authorization_url

    def callback(self):
        slack = OAuth2Session(client_id, state=self.state)
        slack.fetch_token()