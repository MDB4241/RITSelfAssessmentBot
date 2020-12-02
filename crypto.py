from cryptography import fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from hashlib import sha256
import base64
import sys

class Crypto:
    def __init__(self, password):
        self.fernet = fernet.Fernet(self.KDF(password))

    def KDF(self,password):
        kdf = PBKDF2HMAC(algorithm=sha256(), length=32, salt=b"thisisastaticsalt", iterations=100)
        key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
        return key

    def decrypt(self, bytes):
        try:
            decrypted = self.fernet.decrypt(bytes).decode()
            return decrypted
        except fernet.InvalidToken:
            print("Incorrect password!")
            sys.exit(10)



    def encrypt(self, bytes):
        return self.fernet.encrypt(bytes)

