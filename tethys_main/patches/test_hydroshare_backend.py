import logging
import requests_mock

from django.test import TestCase
from django.contrib.auth.models import User

from social.p3 import urlparse
from social.actions import do_auth, do_complete
from social.utils import module_member, parse_qs
from social.strategies.django_strategy import DjangoStrategy
from social.apps.django_app.default.models import DjangoStorage


logger = logging.getLogger(__name__)


@requests_mock.Mocker()
class HydroShareBackendTest(TestCase):

    def setUp(self):

        self.backend_module_path = "tethys_services.backends.hydroshare.HydroShareOAuth2"
        self.Backend_Class = module_member(self.backend_module_path)
        self.auth_server_full_url = self.Backend_Class.auth_server_full_url
        self.client_complete_url = "https://apps.hydroshare.org/complete/hydroshare/"
        self.authorization_code = "my_authorization_code"
        self.access_token = "my_access_token"
        self.refresh_token = "my_refresh_token"
        self.expires_in = 30
        self.social_username="drew123"
        self.social_email="drew123@byu.edu"

    def test_oauth_create_new_user(self, m):
        # test: oauth should create a new user

        # expect for only 1 user: anonymous user
        self.assertEqual(User.objects.all().count(), 1)

        self.run_oauth(m)

        # expect for 2 users: anonymous and newly created social user
        self.assertEqual(User.objects.all().count(), 2)
        self.assertEqual(User.objects.filter(username=self.social_username).count(), 1)
        user = User.objects.filter(username=self.social_username).first()
        self.assertEqual(user.email, self.social_email)

    def test_oauth_create_duplicate_user(self, m):
        # test: if django already has a user with the same username as social_user,
        #       to avoid duplication, a new user should be created with a random string
        #       appended to its username

        # expect for only 1 user: anonymous user
        self.assertEqual(User.objects.all().count(), 1)
        # manually create a new user named self.social_username
        self.user = User.objects.create_user(username=self.social_username,
                                             email=self.social_email,
                                             password='top_secret')
        # expect for 2 users: anonymous and self.social_username
        self.assertEqual(User.objects.all().count(), 2)

        username_new, social = self.run_oauth(m)

        # expect for 3 users
        self.assertEqual(User.objects.all().count(), 3)

        self.assertEqual(User.objects.filter(username=username_new).count(), 1)
        self.assertTrue(len(username_new) > len(self.social_username))
        self.assertEqual(username_new[0:len(self.social_username)], self.social_username)

    def test_oauth_connect_to_existing_user(self, m):

        # expect for only 1 user: anonymous user
        self.assertEqual(User.objects.all().count(), 1)
        # manually create a new user named self.social_username
        user_sherry = User.objects.create_user(username="sherry",
                                             email="sherry@byu.edu",
                                             password='top_secret')
        logger.debug(user_sherry.is_authenticated())
        logger.debug(user_sherry.is_active)

        # expect for 2 users: anonymous and sherry
        self.assertEqual(User.objects.all().count(), 2)

        username_new, social = self.run_oauth(m, user=user_sherry)

        # expect for 2 users
        self.assertEqual(User.objects.all().count(), 2)
        self.assertEqual(social.user, user_sherry)


    def run_oauth(self, m, user=None):

        strategy = DjangoStrategy(DjangoStorage)
        backend = self.Backend_Class(strategy, redirect_uri=self.client_complete_url)

        start_url = do_auth(backend).url
        start_query = parse_qs(urlparse(start_url).query)
        # logger.debug("start_url: {0}".format(start_url))
        #
        # # add authorization code
        # self.client_complete_url += "?code={0}".format(self.authorization_code)
        # # add state parameter
        # self.client_complete_url = self.client_complete_url + \
        #                            ('?' in self.client_complete_url and '&' or '?') + \
        #                            'state=' + start_query['state']
        # logger.debug("client_complete_url: {0}".format(self.client_complete_url))
        #
        # logger.debug(backend.AUTHORIZATION_URL)
        # m.get(backend.AUTHORIZATION_URL, headers={'location': self.client_complete_url}, status_code=301)
        # m.get(self.client_complete_url, text=self.authorization_code, status_code=200)
        #
        # response = requests.get(start_url)
        # self.assertEqual(response.status_code, 200)
        # self.assertEqual(response.url, self.client_complete_url)
        # self.assertEqual(response.text, self.authorization_code)

        # set 'state' in client
        backend.data.update({'state': start_query['state']})

        m.get(backend.USER_DATA_URL,
              json={"username": self.social_username,
                    "email": self.social_email},
              status_code=200)

        m.post(backend.ACCESS_TOKEN_URL,
               json={'access_token': self.access_token,
                     'token_type': 'bearer',
                     'expires_in': self.expires_in,
                     'scope': "read write",
                     'refresh_tocken': self.refresh_token},
               status_code=200)

        def _login(backend, user, social_user):
            backend.strategy.session_set('username', user.username)

        do_complete(backend, user=user, login=_login)
        # self.assertEqual(strategy.session_get('username'),
        #                  "drew123")

        social = backend.strategy.storage.user.get_social_auth(backend.name, self.social_username)

        return strategy.session_get('username'), social

