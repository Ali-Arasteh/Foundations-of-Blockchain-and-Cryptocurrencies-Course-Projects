from sys import exit
from bitcoin.core.script import *

from utils import *
from config import *

from ex1 import (send_from_P2PKH_transaction, P2PKH_scriptPubKey)

import hashlib
import math

n = 14
string = []
N = 2 ** math.ceil(math.log(int(n), 2))
for i in range(1, N + 1):
    if i <= n:
        fileID = open('data\data' + str(i) + '.hex', 'rb')
        string.append(hashlib.sha256(fileID.read()).digest())
        fileID.close()
    else:
        string.append(string[2 * n - i - 1])
for i in reversed(range(int(math.log(N, 2)) + 1)):
    if i == int(math.log(N, 2)):
        for j in range(2 ** i):
            string[j] = hashlib.sha256(string[j]).digest()
    else:
        temp = []
        for j in range(2 ** i):
            temp.append(hashlib.sha256(string[2 * j] + string[2 * j + 1]).digest())
        merkle_root = temp[0]

######################################################################
# TODO: Complete the scriptPubKey implementation for Exercise 9
file_hash_private_key = CBitcoinSecret.from_secret_bytes(merkle_root)
file_hash_public_key = file_hash_private_key.pub
file_hash_address = P2PKHBitcoinAddress.from_pubkey(file_hash_public_key)
######################################################################

if __name__ == '__main__':
    ######################################################################
    # TODO: set these parameters correctly
    amount_to_send = 0.00000001 # amount of BTC in the output you're splitting minus fee
    txid_to_spend = ('c84f49dd740db9735ac3f301517151bfea3bf4802f7311774439f9768be39be9')
    utxo_index = 10 # index of the output you are spending, indices start at 0
    ######################################################################

    txout_scriptPubKey = P2PKH_scriptPubKey(file_hash_address)
    response = send_from_P2PKH_transaction(amount_to_send, txid_to_spend, utxo_index, txout_scriptPubKey, my_private_key, network_type)
    print(response.status_code, response.reason)
    print(response.text)