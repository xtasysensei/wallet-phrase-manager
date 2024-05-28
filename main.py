import json
import os
from core.core import *

def start():
    print("Welcome to phraser")
    wallet_name = input("Which wallet do you want to save phrases for: ")

    wallet_init = WalletName(wallet_name)
    wallet_init.create_wallet()

    while True:
        try:
            phrase_amount = int(input("How many phrases do you want to save (between 12 to 24)?: "))
            if 12 <= phrase_amount <= 24:
                break
            else:
                print("Please enter a valid number (12, 14, 24).")
        except ValueError:
            print("Invalid input. Please enter a number (12, 14, 24).")

    hash_password = input("Enter passphrase that will be used to hash your wallet: ")

    init_wallet = InitializeWallet()
    init_wallet.initialize_wallet(phrase_amount, wallet_name, hash_password)


if __name__ == "__main__":
    start()
