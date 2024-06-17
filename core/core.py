from getpass_asterisk.getpass_asterisk import getpass_asterisk
from lib.colors import *
from lib.jsonManage import *


class WalletName:
    def __init__(self, wallet_name):
        self.wallet_name = wallet_name

    def create_wallet(self):
        print(f"{green}Creating store for{end} {blue}{self.wallet_name.upper()}{end}...")


class InitializeWallet:
    def initialize_wallet(self, phrase_amount, wallet_name, hash_password):
        self.phrase_amount = phrase_amount
        self.wallet_name = wallet_name
        self.hash_password = hash_password

        phrase_array = []

        i = 0
        while i < self.phrase_amount:
            phrases = input(f"Enter phrase {i + 1}: ")
            phrase_array.append(phrases)
            i += 1

        phrase_dict = {self.wallet_name: {f'phrase{i}': phrase_array[i] for i in range(phrase_amount)}}

        manage_json = JsonManage()
        while True:
            confirm_hash_password = getpass_asterisk(f"=> {purple}Confirm your hash password:{end} ")
            if confirm_hash_password == self.hash_password:
                break
            else:
                print("Hash password incorrect, try again")

        is_encrypted = manage_json.is_file_encrypted('data/data.json')
        if is_encrypted:
            manage_json.decrypt_json_file(self.hash_password, 'data/data.json')
            manage_json.append_to_json('data/data.json', phrase_dict)
            manage_json.encrypt_json_file(self.hash_password, 'data/data.json')
        else:
            manage_json.append_to_json('data/data.json', phrase_dict)
            manage_json.encrypt_json_file(self.hash_password, 'data/data.json')
        print(phrase_dict)


class RetrieveWallet:
    def retrieve_wallet(self, hash_password, wallet_name):
        self.hash_password = hash_password
        self.wallet_name = wallet_name
        while True:
            confirm_hash_password = getpass_asterisk(f"=> {purple}Confirm your hash password:{end} ")
            if confirm_hash_password == self.hash_password:
                break
            else:
                print("Hash password incorrect, try again")
        manage_json = JsonManage()
        manage_json.decrypt_json_file(self.hash_password, "data/data.json")
        with open("data/data.json", "r") as f:
            data = json.load(f)
        if self.wallet_name in data:
            wallet_data = data[self.wallet_name]
            print(f"Wallet '{self.wallet_name.upper()}' details:\n")
            for i, (key, value) in enumerate(wallet_data.items(), start=1):
                print(f"[{i}] Phrase{i}  => {value}")
        else:
            print(f"Wallet named '{self.wallet_name}' not found.")
        manage_json.encrypt_json_file(self.hash_password, 'data/data.json')
