from sys import exit
from bitcoin.core.script import *
from bitcoin.wallet import P2PKHBitcoinAddress

from utils import *
from config import *

from ex1 import (P2PKH_scriptPubKey, P2PKH_scriptSig)
from ex6a import (Q6a_txout_scriptPubKey, hamed_private_key)


######################################################################
# TODO: set these parameters correctly
amount_to_send = 0.00025 # amount of BTC in the output you're splitting minus fee
txid_to_spend = ('0361ddeb56b382ce32d3e9398537d2e10a95852408656aee7666450d3ce7d4d3')
utxo_index = 0 # index of the output you are spending, indices start at 0
######################################################################
txout_scriptPubKey = P2PKH_scriptPubKey(my_address)
txout = create_txout(amount_to_send, txout_scriptPubKey)

txin_scriptPubKey = Q6a_txout_scriptPubKey
txin = create_txin(txid_to_spend, utxo_index)
my_signature = create_OP_CHECKSIG_signature(txin, txout, txin_scriptPubKey, my_private_key)
hamed_signature = create_OP_CHECKSIG_signature(txin, txout, txin_scriptPubKey, hamed_private_key)


txin_scriptSig = [my_signature, my_public_key, hamed_signature]
response = send_from_custom_transaction(amount_to_send, txid_to_spend, utxo_index, txin_scriptPubKey, txin_scriptSig, txout_scriptPubKey, network_type)
print(response.status_code, response.reason)
print(response.text)
