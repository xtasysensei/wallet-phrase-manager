import json
import base64
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet


def derive_key(password):
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


def decrypt_json_file(password, json_file):
    key = derive_key(password)
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


decrypt_json_file("shem", "data.json")
with open("data.json", "r") as f:
    data = json.load(f)
    json_data = json.dumps(data, indent=4)
    print(json_data)
