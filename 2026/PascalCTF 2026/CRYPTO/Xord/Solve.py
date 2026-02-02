import os
import random

def xor(a, b):
    return bytes([a ^ b])

random.seed(1337)
ciphertext = bytes.fromhex('cb35d9a7d9f18b3cfc4ce8b852edfaa2e83dcd4fb44a35909ff3395a2656e1756f3b505bf53b949335ceec1b70e0')

encripted_flag = b""
for i in range(len(ciphertext)):
    random_key = random.randint(0, 255)
    encripted_flag += xor(ciphertext[i], random_key)

print(encripted_flag)