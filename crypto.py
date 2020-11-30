from cryptography import fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from hashlib import sha256
import base64

class Crypto:
    def __init__(self, password,salt):
        self.salt = salt.encode()
        self.fernet = fernet.Fernet(self.KDF(password))

    def KDF(self,password):
        kdf = PBKDF2HMAC(algorithm=sha256(), length=32, salt=self.salt, iterations=100)
        key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
        return key

    def encrypt(self, bytes):
        return self.fernet.encrypt(bytes)

    def decrypt(self, bytes):
        return self.fernet.decrypt(bytes)
