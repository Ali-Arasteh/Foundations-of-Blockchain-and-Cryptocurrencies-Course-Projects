from sys import exit
from bitcoin.core.script import *

from utils import *
from config import *

from ex1 import send_from_P2PKH_transaction

######################################################################
# TODO: Complete the scriptPubKey implementation for Exercise 31
Q31a_txout_scriptPubKey = [OP_DUP, faraz_public_key, OP_CHECKSIG, OP_IF, OP_1, OP_ELSE, ata_public_key, OP_CHECKSIGVERIFY, OP_3,
    shareholder5_public_key, shareholder4_public_key, shareholder3_public_key, shareholder2_public_key, shareholder1_public_key,
    OP_5, OP_CHECKMULTISIG, OP_ENDIF]
######################################################################

if __name__ == '__main__':
    ######################################################################
    # TODO: set these parameters correctly
    amount_to_send = 0.0005 # amount of BTC in the output you're splitting minus fee
    txid_to_spend = ('c84f49dd740db9735ac3f301517151bfea3bf4802f7311774439f9768be39be9')
    utxo_index = 2 # index of the output you are spending, indices start at 0
    ######################################################################

    response = send_from_P2PKH_transaction(amount_to_send, txid_to_spend, utxo_index, Q31a_txout_scriptPubKey, my_private_key, network_type)
    print(response.status_code, response.reason)
    print(response.text)
