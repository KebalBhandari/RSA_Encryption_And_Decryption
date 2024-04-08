from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii
import time
start_time = time.time()
key = RSA.generate(1024) 
public_key = key.publickey()
message = 'Hello World !'
encryptor = PKCS1_OAEP.new(public_key)
encrypted_message = encryptor.encrypt(message.encode())
print("Encrypted:", binascii.hexlify(encrypted_message))
decryptor = PKCS1_OAEP.new(key)
decrypted_message = decryptor.decrypt(encrypted_message)
print("Decrypted:", decrypted_message.decode())
print("--- %s seconds ---" % (time.time() - start_time))
