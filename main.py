import json
from collections import defaultdict


def start():
    print("Welcome to phraser")
    wallet_name = input("which wallet do you want to save phrase for: ")

    wallet_init = WalletName(wallet_name)
    wallet_init.create_wallet()

    phrase_amount = int(input("How many phrases do you want to save(12,14,24)?: "))
    hash_password = str(
        input("Enter passphrase that will be used to hash your wallet: ")
    )

    init_wallet = InitializeWallet()
    init_wallet.initialize_wallet(phrase_amount, wallet_name, hash_password)


class WalletName:
    def __init__(self, wallet_name):
        self.wallet_name = wallet_name

    def create_wallet(self):
        print("Creating store for {}...".format(self.wallet_name))


class InitializeWallet:
    def initialize_wallet(self, phrase_amount, wallet_name, hash_password):
        self.phrase_amount = phrase_amount
        self.wallet_name = wallet_name
        self.hash_password = hash_password

        phrase_dict = {}

        # List of items to loop over

        def dynamic_nested_dict():
            nested_dict = defaultdict(lambda: defaultdict(dict))
            return nested_dict

        # Create a nested dictionary
        nested_dict = dynamic_nested_dict()

        # Add items to the nested dictionary
        for i in range(12):
            nested_dict['{}'.format(self.wallet_name)]['phrase{}'.format(i)] = 'value*'

        def append_to_json(filename, data):
            # Read existing data
            with open(filename, 'r') as f:
                existing_data = json.load(f)

            existing_data.update(data)
            with open(filename, 'w') as f:
                json.dump(existing_data, f)

        append_to_json('data.json', nested_dict)
        print(dict(nested_dict))

        # with open("data.json", "a") as outfile:
        #     json.dump(nested_dict, outfile)


if __name__ == "__main__":
    start()
