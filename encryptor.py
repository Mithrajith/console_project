from cryptography.fernet import Fernet

class Encryptor:
    def __init__(self, key_file='key.key'):
        try:
            self.key = open(key_file, 'rb').read()
        except FileNotFoundError:
            self.key = Fernet.generate_key()
            open(key_file, 'wb').write(self.key)
        self.fernet = Fernet(self.key)

    def encrypt(self, data: bytes) -> bytes:
        return self.fernet.encrypt(data)

    def decrypt(self, token: bytes) -> bytes:
        return self.fernet.decrypt(token)
