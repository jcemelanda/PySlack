import re
from unittest import main
from unittest.case import TestCase

from authentication import Authentication

__author__ = 'julio'


class TestAuthentication(TestCase):
    '''
    Test for Slack Authentication Method
    '''

    def test_login(self):
        auth = Authentication()
        login_url = auth.login()
        print(login_url)
        match = re.search(r'https://slack\.com/oauth/authorize\?response_type=code&client_id=.*&state=.*', login_url).group()
        self.assertEqual(match, login_url)

if __name__ == '__main__':
    main()