from sys import exit
from bitcoin.core.script import *
from bitcoin.wallet import P2PKHBitcoinAddress

from utils import *
from config import (my_private_key, my_public_key, my_address, faucet_address, network_type)

from ex1 import (send_from_P2PKH_transaction, P2PKH_scriptPubKey, P2PKH_scriptSig)
from ex5a import (hamed_private_key, hamed_public_key, Q5a_txout_scriptPubKey)


######################################################################
# TODO: set these parameters correctly
amount_to_send = 0.00025 # amount of BTC in the output you're splitting minus fee
txid_to_spend = ('a764e5083a82bd5336210290f5850f41234d0a686effe7cbc950ba9714a61609')
utxo_index = 0 # index of the output you are spending, indices start at 0
######################################################################

def send_from_P2PKH_transaction(amount_to_send,
                                txid_to_spend,
                                utxo_index,
                                txout_scriptPubKey,
                                sender_private_key,
                                network):

    sender_public_key = sender_private_key.pub
    sender_address = P2PKHBitcoinAddress.from_pubkey(sender_public_key)

    txout = create_txout(amount_to_send, txout_scriptPubKey)

    txin_scriptPubKey = Q5a_txout_scriptPubKey
    txin = create_txin(txid_to_spend, utxo_index)
    txin_scriptSig = P2PKH_scriptSig(txin, txout, txin_scriptPubKey, sender_private_key, sender_public_key)

    new_tx = create_signed_transaction(txin, txout, txin_scriptPubKey, txin_scriptSig)

    return broadcast_transaction(new_tx, network)


txout_scriptPubKey = P2PKH_scriptPubKey(faucet_address)
response = send_from_P2PKH_transaction(amount_to_send, txid_to_spend, utxo_index, txout_scriptPubKey, hamed_private_key, network_type)
print(response.status_code, response.reason)
print(response.text)
