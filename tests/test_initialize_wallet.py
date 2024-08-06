from core.core import WalletName, InitializeWallet


class TestWalletName:
    def test_create_wallet(self):
        c = WalletName("shem")
        print("testing wallet creation : create wallet")
        assert 'shem' == c.wallet_name


class TestInitializeWallet:
    def test_initialize_wallet(self):
        i = InitializeWallet()
        print("testing wallet initialization : initialize wallet")

