from core.core import *
from lib.colors import *


def lines():
    print("|----------------------------------|")


def retrieve_wallet(hash_password_param):
    wallet_name = input(f"=> {purple}Which wallet do you want to retrieve:{end} ")
    print(f"{green}Retrieving phrases for{end} {blue}{wallet_name.upper()}{end}...")
    wallet_get = RetrieveWallet()
    wallet_get.retrieve_wallet(hash_password_param, wallet_name)


def delete_wallet(hash_password_param):
    wallet_name = input(f"=> {purple}Which wallet do you want to remove:{end} ")
    remove_wallet = DeleteWallet()
    remove_wallet.delete_wallet(hash_password_param, wallet_name)


def add_wallet(hash_password_param):
    wallet_name = input(f"=> {purple}Which wallet do you want to save phrases for:{end} ")
    wallet_init = WalletName(wallet_name)
    wallet_init.create_wallet()

    while True:
        try:
            phrase_amount = int(input(f"=> {purple}How many phrases do you want to save (between 12 to 24)?:{end} "))
            if 12 <= phrase_amount <= 24:
                break
            else:
                print(f"{red}[!] Please enter a valid number (12, 14, 24).{end}")
        except ValueError:
            print(f"{red}[!] Invalid input!!{end} Please enter a number (12, 14, 24).")

    hash_password = hash_password_param

    init_wallet = InitializeWallet()
    init_wallet.initialize_wallet(phrase_amount, wallet_name, hash_password)


def exit_message():
    lines()
    print(f"    {red}Exiting PhraSer...{end}")
    lines()
    sys.exit()


def start():
    while True:
        lines()
        print(f"{green}    Welcome to PhraSer{end}")
        lines()
        global_hash_password = getpass_asterisk(
            f"=> {purple}Enter passphrase that will be used to encrypt/decrypt:{end} ")
        try:
            print(f"{blue}|---------------MENU---------------|{end}")
            print(f"  What do you want to do?")
            print(f"{gray}    [1] {cyan}Add wallet{end}")
            print(f"{gray}    [2] {cyan}Retrieve wallet{end}")
            print(f"{gray}    [3] {cyan}Remove wallet{end}")
            print(f"{red}    [q] Exit{end}")
            lines()
            choice: str = input("option:> ")
            if choice not in ('1', '2', '3', 'q'):
                print("=> Please enter an option (1, 2, 3, q)")
            else:
                break
        except ValueError:
            print(f"{red}[!]Invalid input!!{end} Please enter a option (1, 2, 3, q).")

    if choice == "1":
        add_wallet(global_hash_password)
    elif choice == "2":
        retrieve_wallet(global_hash_password)
    elif choice == "3":
        delete_wallet(global_hash_password)
    elif choice == "q":
        exit_message()
    else:
        print(f"{red}[!]Invalid input!!{end} Please enter a option (1, 2, 3, q).")


if __name__ == "__main__":
    try:
        start()
    except KeyboardInterrupt:
        print("")
        exit_message()
