from sys import exit
from bitcoin.core.script import *

from utils import *
from config import *

from ex1 import send_from_P2PKH_transaction
from bitcoin.wallet import CBitcoinSecret, P2PKHBitcoinAddress

######################################################################
# TODO: Complete the scriptPubKey implementation for Exercise 5
hamed_private_key = CBitcoinSecret('cPnhV6oJnyXFWHnLfhZkXqgbdXarogtu1mtZgUXeYndeFhDATpFv')
hamed_public_key = hamed_private_key.pub
hamed_address = P2PKHBitcoinAddress.from_pubkey(hamed_public_key)
Q6a_txout_scriptPubKey = [OP_DUP, hamed_public_key, OP_CHECKSIG, OP_NOTIF, 1607075400000, OP_CHECKLOCKTIMEVERIFY, OP_ENDIF, OP_DROP, OP_DUP, OP_HASH160, my_address, OP_EQUALVERIFY, OP_CHECKSIG]
######################################################################

if __name__ == '__main__':
    ######################################################################
    # TODO: set these parameters correctly
    amount_to_send = 0.0005 # amount of BTC in the output you're splitting minus fee
    txid_to_spend = ('c84f49dd740db9735ac3f301517151bfea3bf4802f7311774439f9768be39be9')
    utxo_index = 11 # index of the output you are spending, indices start at 0
    ######################################################################

    response = send_from_P2PKH_transaction(amount_to_send, txid_to_spend, utxo_index, Q6a_txout_scriptPubKey, my_private_key, network_type)
    print(response.status_code, response.reason)
    print(response.text)
