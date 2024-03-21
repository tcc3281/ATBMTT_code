import math

from modernblockcode import AES
from modernblockcode import DES
from modulararithmetic import Module

def des():
    print("DES:")
    plaintext = '0123456789ABCDEF'
    ciphertext = '85E813540F0AB405'
    key = '133457799BBCDFF1'
    print('plaintext: ' + plaintext)
    p = DES.encode(plaintext, key)
    print(f'encode: {p}')
    c = DES.decode(ciphertext, key)
    print(f'decode: {c}')


def aes():
    print('AES:')
    plaintext = '3243f6a8885a308d313198a2e0370734'
    ciphertext = '3925841D02DC09FBDC118597196A0B32'
    key = '2b7e151628aed2a6abf7158809cf4f3c'
    print('plaintext: ' + plaintext)
    p = AES.encode(plaintext, key)
    print(f'encode: {p}')
    c = AES.decode(ciphertext, key)
    print(f'decode: {c}')


if __name__ == '__main__':
    des()
    aes()

