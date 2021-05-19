# Реализовать криптосистему RSA для шифрования и расшифрования вводимых сообщений. Открытый ключ показывать пользователю, закрытый ключ записывать в файл.

# from ecdsa import SigningKey, NIST384p, BadSignatureError
#
# sk = SigningKey.generate(curve=NIST384p)
# vk = sk.verifying_key
# signature = sk.sign(b"message")
#
# try:
#     assert vk.verify(signature, b"message")
#     print('Цифровая подпись прошла проверку')
# except BadSignatureError:
#     print("Цифровая подпись не прошла проверку")
#

import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random

random_generator = Random.new().read
key = RSA.generate(1024, random_generator)  # generate public and private keys

publickey = key.publickey  # pub key export for exchange

encrypted = publickey.encrypt('encrypt this message', 32)
# message to encrypt is in the above line 'encrypt this message'

print('encrypted message:', encrypted)  # ciphertext

f = open('encryption.txt', 'w', w)
f.write(str(encrypted))  # write ciphertext to file
f.close()

# decrypted code below

f = open('encryption.txt', 'r')
message = f.read()

decrypted = key.decrypt(message)

print('decrypted', decrypted)

f = open('encryption.txt', 'w')
f.write(str(message))
f.write(str(decrypted))
f.close()
