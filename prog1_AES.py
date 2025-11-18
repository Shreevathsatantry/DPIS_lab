from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

key=get_random_bytes(16)
data=b'This is a secret message.'
c=AES.new(key,AES.MODE_EAX)
ct,t=c.encrypt_and_digest(data)
print("Ciphertext: ",ct)
print("Decrypted: ",(AES.new(key,AES.MODE_EAX,nonce=c.nonce)).decrypt_and_verify(ct,t).decode())
