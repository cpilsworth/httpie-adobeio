from adobeio import AdobeIOToken
from httpie.plugins import AuthPlugin


class AdobeIOAuth:
    def __init__(self, profile, secret_key):
        self.secret_key = secret_key
        self.adobeio = AdobeIOToken(profile)

    def __call__(self, r):
        auth_headers = self.adobeio.get_headers(self.secret_key)
        r.headers.update(auth_headers)
        return r


class AdobeIOAuthPlugin(AuthPlugin):
    name = "Adobe IO auth"
    auth_type = "adobeio"
    description = "Authenticate with the adobeio api"
    auth_require = False
    prompt_password = True

    def get_auth(self, username=None, password=None):
        return AdobeIOAuth(username, password)
