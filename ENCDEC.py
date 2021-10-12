import binascii
import os
import time
import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES
from secretsharing import PlaintextToHexSecretSharer
from secretsharing import SecretSharer

#   AES METHOD

class AESCipher(object):

    def __init__(self, key):
        self.k = key
        self.bs = AES.block_size
        self.key = self.k.encode("utf-8")
        
    def encrypt(self, raw):
        raw = self._pad(raw)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        enc = cipher.encrypt(raw.encode())
        return base64.b64encode(iv + enc).decode('utf-8')

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        iv = enc[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        dec = cipher.decrypt(enc[AES.block_size:])
        return self._unpad(dec).decode('utf-8')

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s)-1:])]
