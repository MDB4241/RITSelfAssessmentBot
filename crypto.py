from cryptography import fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from hashlib import sha256
import base64

class Crypto:
    def __init__(self, password):
        self.fernet = fernet.Fernet(self.KDF(password))

    def KDF(self,password):
        kdf = PBKDF2HMAC(algorithm=sha256(), length=32, salt=b"thisisastaticsalt", iterations=100)
        key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
        return key

    # def encrypt_to_file(self, filename, bytes):
    #     with open(filename,'wb') as config:
    #         config.write(self.fernet.encrypt(bytes))
    #
    # def decrypt_to_mem(self, filename,bytes):
    #     # TODO return (username,password)
    #     with open(filename,'rb') as config:
    #         temp = self.fernet.decrypt(bytes)
    #     return None

    def encrypt(self, bytes):
        return self.fernet.encrypt(bytes)

    def decrypt(self, bytes):
        return self.fernet.decrypt(bytes)

