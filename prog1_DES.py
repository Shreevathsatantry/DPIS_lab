from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

key = b'8bytekey'
data = b'Shreevathsa'
c = DES.new(key, DES.MODE_ECB)
ct = c.encrypt(pad(data, DES.block_size))
print("Encrypted:", ct)
print("Decrypted:", unpad(c.decrypt(ct), DES.block_size))






