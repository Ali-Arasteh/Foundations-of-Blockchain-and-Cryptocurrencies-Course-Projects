from sys import exit
from bitcoin.core.script import *

from utils import *
from config import (my_private_key, my_public_key, my_address, faucet_address, network_type)
                    
from ex1 import send_from_P2PKH_transaction

######################################################################
# TODO: Complete the scriptPubKey implementation for Exercise 4
string = input('Enter your message: ').encode('UTF-8')
Q4_txout_scriptPubKey = [OP_RETURN, string]
######################################################################

if __name__ == '__main__':
    ######################################################################
    # TODO: set these parameters correctly
    amount_to_send = 0.0005 # amount of BTC in the output you're splitting minus fee
    txid_to_spend = ('c84f49dd740db9735ac3f301517151bfea3bf4802f7311774439f9768be39be9')
    utxo_index = 5 # index of the output you are spending, indices start at 0
    ######################################################################

    response = send_from_P2PKH_transaction(amount_to_send, txid_to_spend, utxo_index, Q4_txout_scriptPubKey, my_private_key, network_type)
    print(response.status_code, response.reason)
    print(response.text)
