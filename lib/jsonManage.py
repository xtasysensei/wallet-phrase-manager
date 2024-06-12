import json
import os
from cryptography.fernet import Fernet


def append_to_json(filename, data):
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


def encrypt_json_file(password, json_file):
    key = Fernet.generate_key(password)
    cipher_suite = Fernet(key)
    with open(json_file, 'rb') as file:
        file_data = file.read()
    encrypted_data = cipher_suite.encrypt(file_data)
    with open(json_file, 'wb') as file:
        file.write(encrypted_data)


def decrypt_json_file(password, json_file):
    key = Fernet.generate_key(password)
    cipher_suite = Fernet(key)
    with open(json_file, 'rb') as file:
        encrypted_data = file.read()
    decrypted_data = cipher_suite.decrypt(encrypted_data)
    with open(json_file, 'wb') as file:
        file.write(decrypted_data)
    return decrypted_data
