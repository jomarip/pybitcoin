#private key
from pybitcoin import BitcoinPrivateKey
private_key = BitcoinPrivateKey()
private_key.to_hex()
private_key.to_wif()
private_key_2 = BitcoinPrivateKey('0031b63c3d6fc66b14f91f352725d57dd865d947d39aab6ced2d5e8b2b3a4261')
print(private_key.to_wif() == private_key_2.to_wif())

#public key
public_key = private_key.public_key()
public_key.to_hex()

------------------------- #Test 2

#private key
from pybitcoin import BitcoinPrivateKey
from pybitcoin import BitcoinPublicKey
private_key = BitcoinPrivateKey()
private_key.to_hex()
private_key.to_wif()

#public key
public_key = private_key.public_key()
public_key.to_hex()
public_key_2 = BitcoinPublicKey(public_key.to_hex())