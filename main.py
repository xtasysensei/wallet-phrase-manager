import sys
from core.core import *
from lib.colors import *


def lines():
    print("----------------------")


def add_wallet():
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


def start():
    while True:
        try:
            print("Welcome to PhraSer")
            print("What do you want to do?")
            print(f"    [1] Add wallet")
            print(f"    [2] Remove wallet")
            print(f"    [3] Retrieve wallet")
            print(f"    [q] Exit")
            choice: str = input("option:> ")
            if choice not in ('1', '2', '3', 'q'):
                print("Please enter an option (1, 2, 3, q)")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a option (1, 2, 3, q).")

    if choice == "1":
        add_wallet()
    #elif choice == "2":
    #elif choice == "3":
    elif choice == "q":
        lines()
        print("Exiting PhraSer...")
        lines()
        sys.exit()
    else:
        print("Invalid input. Please enter a option (1, 2, 3, q).")


if __name__ == "__main__":
    start()
