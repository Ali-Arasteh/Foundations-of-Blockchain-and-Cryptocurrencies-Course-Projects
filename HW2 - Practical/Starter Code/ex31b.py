from sys import exit
from bitcoin.core.script import *

from utils import *
from config import *

from ex1 import P2PKH_scriptPubKey
from ex31a import Q31a_txout_scriptPubKey

######################################################################
# TODO: set these parameters correctly
amount_to_send = 0.00025 # amount of BTC in the output you're splitting minus fee
txid_to_spend = ('91b4442f63f9aa399b9750b9f2946c04e70a4a28457beeff310341076e6070ef')
utxo_index = 0 # index of the output you are spending, indices start at 0
######################################################################

######################################################################
# TODO: implement the scriptSig for redeeming the transaction created
# in  Exercise 31a.
txout_scriptPubKey = P2PKH_scriptPubKey(faucet_address)
txout = create_txout(amount_to_send, txout_scriptPubKey)

txin_scriptPubKey = Q31a_txout_scriptPubKey
txin = create_txin(txid_to_spend, utxo_index)
faraz_signature = create_OP_CHECKSIG_signature(txin, txout, txin_scriptPubKey, faraz_private_key)
ata_signature = create_OP_CHECKSIG_signature(txin, txout, txin_scriptPubKey, ata_private_key)
shareholder1_signature = create_OP_CHECKSIG_signature(txin, txout, txin_scriptPubKey, shareholder1_private_key)
shareholder2_signature = create_OP_CHECKSIG_signature(txin, txout, txin_scriptPubKey, shareholder2_private_key)
shareholder3_signature = create_OP_CHECKSIG_signature(txin, txout, txin_scriptPubKey, shareholder3_private_key)
shareholder4_signature = create_OP_CHECKSIG_signature(txin, txout, txin_scriptPubKey, shareholder4_private_key)
shareholder5_signature = create_OP_CHECKSIG_signature(txin, txout, txin_scriptPubKey, shareholder5_private_key)

txin_scriptSig = [0, shareholder5_signature, shareholder3_signature, shareholder1_signature, ata_signature]
######################################################################

response = send_from_custom_transaction(amount_to_send, txid_to_spend, utxo_index, txin_scriptPubKey, txin_scriptSig, txout_scriptPubKey, network_type)
print(response.status_code, response.reason)
print(response.text)
