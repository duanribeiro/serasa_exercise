from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet
import base64


class AuthEncrypt:
    def __init__(self, password='password'):
        self.password = password

        salt = b'salt_'
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=default_backend()
        )
        key = base64.urlsafe_b64encode(kdf.derive('secret-key'.encode()))
        self.f = Fernet(key)


    def encrypt_password(self):
        self.encrypted = self.f.encrypt(self.password).decode()
        return self.encrypted


    def decrypt_password(self, password):
        return self.f.decrypt(password.encode()).decode()
