from bitcoin import SelectParams
from bitcoin.base58 import decode
from bitcoin.core import x
from bitcoin.wallet import CBitcoinAddress, CBitcoinSecret, P2PKHBitcoinAddress


SelectParams('testnet')

faucet_address = CBitcoinAddress('mv4rnyY3Su5gjcDNzbMLKBQkBicCtHUtFB')

# For questions 1-3, we are using 'btc-test3' network. For question 4, you will
# set this to be either 'btc-test3' or 'bcy-test'
network_type = 'btc-test3'


######################################################################
# This section is for Questions 1-3
# TODO: Fill this in with your private key.
#
# Create a private key and address pair in Base58 with keygen.py
# Send coins at https://coinfaucet.eu/en/btc-testnet/

my_private_key = CBitcoinSecret('cVtSh4gTNUTp2XBjJo2FtDmJp9Tmt12BFSEKEi4rrE8YxQj43D61')
my_public_key = my_private_key.pub
my_address = P2PKHBitcoinAddress.from_pubkey(my_public_key)
######################################################################


######################################################################
# NOTE: This section is for Question 10
# TODO: Fill this in with address secret key for BTC testnet3
#
# Create address in Base58 with keygen.py
# Send coins at https://coinfaucet.eu/en/btc-testnet/

# Only to be imported by alice.py
# Alice should have coins!!
alice_secret_key_BTC = CBitcoinSecret('cVYzJgkCDEaqW8wRhLWTeGVkSySmqqjt6WqX6yx9fXQ6fuHfLLXN')

# Only to be imported by bob.py
bob_secret_key_BTC = CBitcoinSecret('cQ3HSxu11TQcmFP63Zy73f4p2ioEavEiJwZbWZ8FSw2qGoUeGhwq')

# Can be imported by alice.py or bob.py
alice_public_key_BTC = alice_secret_key_BTC.pub
alice_address_BTC = P2PKHBitcoinAddress.from_pubkey(alice_public_key_BTC)

bob_public_key_BTC = bob_secret_key_BTC.pub
bob_address_BTC = P2PKHBitcoinAddress.from_pubkey(bob_public_key_BTC)
######################################################################

faraz_private_key = CBitcoinSecret('cQSGYsYCriYZoyTkXkAexq1EKeVjRezbfjzCfBHjh7994SZKRjxc')
faraz_public_key = faraz_private_key.pub
faraz_address = P2PKHBitcoinAddress.from_pubkey(faraz_public_key)
ata_private_key = CBitcoinSecret('cTUtzKWMpZqCt8Yc61DJokxQszK4TwEnN2FDs1wwRXe2URpMw1cS')
ata_public_key = ata_private_key.pub
ata_address = P2PKHBitcoinAddress.from_pubkey(ata_public_key)
shareholder1_private_key = CBitcoinSecret('cRHzcK6nQ8WwfoUfFTQkDc1NFrn2REGQ4SwG6zDqNLaxY5RY8UXm')
shareholder1_public_key = shareholder1_private_key.pub
shareholder1_address = P2PKHBitcoinAddress.from_pubkey(shareholder1_public_key)
shareholder2_private_key = CBitcoinSecret('cV1NZicTfXPHGnoY6rWKujwGRgARSTNQX93WZPwELNZ4qBCvnWRk')
shareholder2_public_key = shareholder2_private_key.pub
shareholder2_address = P2PKHBitcoinAddress.from_pubkey(shareholder2_public_key)
shareholder3_private_key = CBitcoinSecret('cPEKuQYYbR9dnPJ4oDrpfh2Lx137JasUMSS8FBpJoyeuNWAef5v6')
shareholder3_public_key = shareholder3_private_key.pub
shareholder3_address = P2PKHBitcoinAddress.from_pubkey(shareholder3_public_key)
shareholder4_private_key = CBitcoinSecret('cMebJty5uzBobC927Rf8JvRbqVFDbz3kfQTJhHc7wXnnn5teRosj')
shareholder4_public_key = shareholder4_private_key.pub
shareholder4_address = P2PKHBitcoinAddress.from_pubkey(shareholder4_public_key)
shareholder5_private_key = CBitcoinSecret('cTk9UTfi686qjnPCGdbPhHkLMFEip8nAPSpYpkAsFkjaXAra2dAU')
shareholder5_public_key = shareholder5_private_key.pub
shareholder5_address = P2PKHBitcoinAddress.from_pubkey(shareholder5_public_key)

######################################################################
# NOTE: This section is for Question 10
# TODO: Fill this in with address secret key for BCY testnet
#
# Create address in hex with
# curl -X POST https://api.blockcypher.com/v1/bcy/test/addrs?token=$YOURTOKEN
# This request will return a private key, public key and address. Make sure to save these.
#
# Send coins with
# curl -d '{"address": "BCY_ADDRESS", "amount": 1000000}' https://api.blockcypher.com/v1/bcy/test/faucet?token=<YOURTOKEN>
# This request will return a transaction reference. Make sure to save this.

# Only to be imported by alice.py
alice_secret_key_BCY = CBitcoinSecret.from_secret_bytes(x('c527635a85bfe389e4cf26d412cf003d2128290d4acecb4875feaed4465028a6'))

# Only to be imported by bob.py
# Bob should have coins!!
bob_secret_key_BCY = CBitcoinSecret.from_secret_bytes(x('f86cba7b7b61f928ac3c209b2e10ce013eeaad5854fe86942633ebc906787e4f'))

# Can be imported by alice.py or bob.py
alice_public_key_BCY = alice_secret_key_BCY.pub
alice_address_BCY = P2PKHBitcoinAddress.from_pubkey(alice_public_key_BCY)

bob_public_key_BCY = bob_secret_key_BCY.pub
bob_address_BCY = P2PKHBitcoinAddress.from_pubkey(bob_public_key_BCY)
######################################################################
