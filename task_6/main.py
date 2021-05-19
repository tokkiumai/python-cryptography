# Реализовать программный продукт построения sha-1 для введенного текста.

import hashlib

m = hashlib.sha1()
m.update(b"super simple sha-1")
encrypted = m.hexdigest()
print(encrypted)
