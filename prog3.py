from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA

key = RSA.generate(2048)
def sign_message(m, k): return PKCS1_v1_5.new(k).sign(SHA256.new(m))
def verify_signature(m, s, k): return PKCS1_v1_5.new(k).verify(SHA256.new(m), s)

message = b'This is a secret message.'
signature = sign_message(message, key)
print("Is signature valid?", verify_signature(message, signature, key.publickey()))
