# -*- coding: utf-8 -*-
import sys
from base64 import b64encode,b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from hashlib import blake2b
import os


def encrypt_mytext(mytext,input_key):
    h = blake2b(digest_size=16)
    h.update(input_key.encode())
    key=h.hexdigest()
    data=mytext+" "
    cipher = AES.new(b64decode(key), AES.MODE_CBC, iv=b'0123456789abcdef')
    padded_data = pad(data.encode("utf-8"), cipher.block_size)
    encrypt_text = cipher.encrypt(padded_data)
    print(type(encrypt_text))
    #print(encrypt_text.decode("utf-8"))
    return encrypt_text


def decrypt_mytext(enctext,input_key):

    ciphertext = enctext
    h = blake2b(digest_size=16)
    h.update(input_key.encode())
    key=h.hexdigest()
    cipher= AES.new(b64decode(key), AES.MODE_CBC, iv=b'0123456789abcdef')
    decrypt_text=str(cipher.decrypt(ciphertext).decode("utf-8")).split(' ')[0]
    return decrypt_text


mytext=input("mytext:")
mykey=input("mykey:")

encrypt_text=encrypt_mytext(mytext,mykey)
decrypt_text=decrypt_mytext(encrypt_text,mykey)
print(encrypt_text.decode("utf-8"))
print(decrypt_text)
        