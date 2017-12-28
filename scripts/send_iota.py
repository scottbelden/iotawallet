import getpass
from iotawallet import Wallet

uri = input('Node URI: ')
seed = getpass.getpass(prompt='Seed: ')

address = input('Receiving adddress: ')
value = int(input('Iota to send: '))

wallet = Wallet(uri, seed)
wallet.send(address=address, value=value)
