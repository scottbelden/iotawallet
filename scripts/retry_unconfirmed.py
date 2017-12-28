import getpass
from iotawallet import Wallet

uri = input('Node URI: ')
seed = getpass.getpass(prompt='Seed: ')

wallet = Wallet(uri, seed)
wallet.retry_unconfirmed_bundles()
