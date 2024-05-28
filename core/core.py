import json
import os

class WalletName:
    def __init__(self, wallet_name):
        self.wallet_name = wallet_name

    def create_wallet(self):
        print(f"Creating store for {self.wallet_name}...")


class InitializeWallet:
    def initialize_wallet(self, phrase_amount, wallet_name, hash_password):
        self.phrase_amount = phrase_amount
        self.wallet_name = wallet_name
        self.hash_password = hash_password

        phrase_dict = {self.wallet_name: {f'phrase{i}': 'value*' for i in range(phrase_amount)}}

        self.append_to_json('data.json', phrase_dict)
        print(phrase_dict)

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
