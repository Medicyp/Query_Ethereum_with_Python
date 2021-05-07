import os
from dotenv import load_dotenv
from web3 import Web3

NODE_PROVIDER_LOCAL = 'YOUR_GANACHE_RPC_SERVER_ID'
PRIVATE_KEY_1='YOUR_SENDER_PRIVATE_KEY'
PUBLIC_KEY_1='YOUR_SENDER_PUBLIC_KEY'
PUBLIC_KEY_2='YOUR_RECEIVER_PUBLIC_KEY'

load_dotenv()

node_provider = NODE_PROVIDER_LOCAL
web3_connection=Web3(Web3.HTTPProvider(node_provider))

global_gas = 4500000
global_gas_price = web3_connection.toWei(8, 'gwei')

def are_we_connected():
    return web3_connection.isConnected()

print(are_we_connected())

def get_nonce(ETH_address):
    return web3_connection.eth.get_transaction_count(ETH_address)

def transfer_ETH(sender, receiver, signature, amount_ETH):
    transaction_body = {
        'nonce': get_nonce(sender),
        'to': receiver,
        'value' : web3_connection.toWei(amount_ETH, 'ether'),
        'gas': global_gas,
        'gasPrice': global_gas_price
    }
    signed_transaction =web3_connection.eth.account.sign_transaction(transaction_body,signature)
    result = web3_connection.eth.send_raw_transaction(signed_transaction.rawTransaction)

    return result

transfer_ETH(PUBLIC_KEY_1, PUBLIC_KEY_2, PRIVATE_KEY_1, 4)

# credits: https://www.youtube.com/watch?v=NkCbZGS70Yc&list=PLFPZ8ai7J-iRa9eb1qTuepB1qaMYfhcWn&index=3
