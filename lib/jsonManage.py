import json
import os
import base64
import binascii
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet


class JsonManage:
    def append_to_json(self, filename, data):
        if not os.path.exists(filename):
            with open(filename, 'w') as f:
                json.dump({}, f)

        try:
            with open(filename, 'r') as f:
                existing_data = json.load(f)
        except json.JSONDecodeError:
            existing_data = {}

        existing_data.update(data)

        try:
            with open(filename, 'w') as f:
                json.dump(existing_data, f, indent=4)
        except IOError as e:
            print(f"An error occurred while writing to the file: {e}")

    def _derive_key(self, password):
        salt = b'some_salt'  # In practice, use a unique salt for each password
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=default_backend()
        )
        key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
        return key

    def encrypt_json_file(self, password, json_file):
        key = self._derive_key(password)
        cipher_suite = Fernet(key)
        try:
            with open(json_file, 'rb') as file:
                file_data = file.read()
            encrypted_data = cipher_suite.encrypt(file_data)
            with open(json_file, 'wb') as file:
                file.write(encrypted_data)
        except Exception as e:
            print(f"An error occurred while encrypting the file: {e}")

    def decrypt_json_file(self, password, json_file):
        key = self._derive_key(password)
        cipher_suite = Fernet(key)
        try:
            with open(json_file, 'rb') as file:
                encrypted_data = file.read()
            decrypted_data = cipher_suite.decrypt(encrypted_data)
            with open(json_file, 'wb') as file:
                file.write(decrypted_data)
            return json.loads(decrypted_data)
        except Exception as e:
            print(f"An error occurred while decrypting the file: {e}")
            return None

    def is_file_encrypted(self, file_path):
        try:
            with open(file_path, 'rb') as file:
                file_data = file.read()

            # Check if the file data is valid base64 (Fernet produces base64-encoded output)
            try:
                base64.urlsafe_b64decode(file_data)
            except binascii.Error:
                return False

            # Optionally, check if the file starts with the expected Fernet prefix
            return file_data.startswith(b'gAAAAAB')

        except Exception as e:
            print(f"An error occurred while checking the file: {e}")
            return False
