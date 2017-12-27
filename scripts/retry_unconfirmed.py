import getpass
from iotawallet import Wallet

uri = input('Node URI: ')
seed = getpass.getpass(prompt='Seed: ')

print('Starting Wallet')
wallet = Wallet(uri, seed)

print(f'Balance: {wallet.balance}')
print(f'Addresses: {wallet.addresses}')
print(f'Bundles: {wallet.bundles}')
print('')

wallet.retry_unconfirmed_bundles()
