# -*- coding:utf-8 -*-
from itsdangerous import URLSafeTimedSerializer as utsr
import base64


class Token():

    def __init__(self, security_key):
        self.security_key = security_key
        self.salt = base64.b64encode(security_key.encode(encoding='utf-8'))

    def confirm_validate_token(self, token):
        serializer = utsr(self.security_key)
        return serializer.loads(token, salt=self.salt)

    def generate_validate_token(self, username, expiration=3600):
        serializer = utsr(self.security_key, expiration)
        return serializer.dumps(username,
                                salt=self.salt)
