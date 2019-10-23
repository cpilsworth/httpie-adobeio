import jwt
import json
import requests
from os import path
from datetime import datetime, timedelta
from configparser import ConfigParser
from cryptography.x509 import load_pem_x509_certificate
from cryptography.hazmat.backends import default_backend


class AdobeIOToken:

    CONFIG_FILE = path.expanduser("~/.httpie_adobeio.ini")

    def __init__(self, profile):
        file = self.CONFIG_FILE
        config = ConfigParser()
        
        if not path.exists(file) or not path.isfile(file):
            raise Exception(f"Could not file configuration file at {file}")
        
        config.read(file)
        if profile not in config:
            raise Exception(f"Could not file profile {profile} in {file}")
        
        self.private_key = config[profile]["private_key"]
        self.public_cert = config[profile]["public_cert"]
        self.ims_base = config[profile]["ims_base"]
        self.org_id = config[profile]["ims_org"]
        self.account_id = config[profile]["account_id"]
        self.api_key = config[profile]["api_key"]
        self.scopes = config[profile]["scopes"].splitlines()

    def request_jwt(self):
        claims = {
            "exp": self._get_expiry(),
            "iss": self.org_id,
            "sub": self.account_id,
            "aud": self._get_audience(),
        }
        scopes = {f"{self.ims_base}/s/{scope}": True for scope in self.scopes}
        token = {**claims, **scopes}
        return jwt.encode(token, self.private_key, algorithm="RS256")

    def access_token(self, secret_key):
        jwt_token = self.request_jwt()
        headers = {"Cache-Control": "no-cache"}
        data = {
            "client_id": self.api_key,
            "client_secret": secret_key,
            "jwt_token": jwt_token,
        }
        response = requests.post(
            f"{self.ims_base}/ims/exchange/jwt/", headers=headers, data=data
        )
        try:
            return json.loads(response.text)["access_token"]
        except KeyError:
            print(response.text)

    def get_headers(self, secret_key):
        return {
            "x-api-key": self.api_key,
            "Authorization": self._authorization_header(secret_key),
            "x-gw-ims-org-id": self.org_id,
        }

    def _get_expiry(self):
        expires = datetime.now() + timedelta(days=1)
        return int(expires.strftime("%s"))

    def _get_audience(self):
        return f"{self.ims_base}/c/{self.api_key}"

    def _authorization_header(self, secret_key):
        jwt = self.access_token(secret_key)
        return f"Bearer {jwt}"

    def _decode(self, jwt_token):
        cert_bytes = bytearray(self.public_cert, "UTF-8")
        cert_obj = load_pem_x509_certificate(cert_bytes, default_backend())
        public_key = cert_obj.public_key()
        audience = self._get_audience()
        return jwt.decode(
            jwt_token, public_key, algorithms=["RS256"], audience=audience
        )
