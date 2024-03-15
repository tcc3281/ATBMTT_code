from modernblockcode import DES

if __name__ == '__main__':
    M = "0123456789ABCDEF"
    K = "133457799BBCDFF1"
    D = "85E813540F0AB405"
    r = DES.encode(M, K)
    print(r)
    p = DES.decode(D, K)
    print(p)
