from modernblockcode import DES

if __name__ == '__main__':
    M = "0123456789ABCDEF"
    K = "133457799BBCDFF1"
    D = "85E813540F0AB405"
    r = DES.encode(M, K)
    print(r)
    p = DES.decode(D, K)
    print(p)

    print("2b 7e 15 16 28 ae d2 a6 ab f7 15 88 09 cf 4f 3c".replace(' ', ''))
