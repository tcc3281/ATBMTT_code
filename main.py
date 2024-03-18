from modernblockcode import AES

if __name__ == '__main__':
    plaintext = "3243f6a8885a308d313198a2e0370734"
    key = '2b7e151628aed2a6abf7158809cf4f3c'
    d = "3925841D02DC09FBDC118597196A0B32"
    r = AES.decode(d, key)
    print(*r, sep='\n')
    print(AES.transText(r))
