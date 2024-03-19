class DES:
    PC_1 = [57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18, 10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36,
            63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22, 14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4]
    PC_2 = [14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2, 41, 52, 31, 37, 47,
            55, 30, 40, 51, 45, 33, 48, 44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]
    Lap = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
    E_BOX = [32, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9, 8, 9, 10, 11, 12, 13, 12, 13, 14, 15, 16, 17, 16, 17, 18, 19, 20, 21,
             20, 21, 22, 23, 24, 25, 24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32, 1]
    S1_BOX = [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7, 0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3,
              8, 4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0, 15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6,
              13]
    S2_BOX = [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10, 3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11,
              5, 0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15, 13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5,
              14, 9]
    S3_BOX = [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8, 13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15,
              1, 13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7, 1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2,
              12]
    S4_BOX = [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15, 13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14,
              9, 10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4, 3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2,
              14]
    S5_BOX = [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9, 14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8,
              6, 4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14, 11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4,
              5, 3]
    S6_BOX = [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11, 10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3,
              8, 9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6, 4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8,
              13]
    S7_BOX = [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1, 13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8,
              6, 1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2, 6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3,
              12]
    S8_BOX = [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7, 1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9,
              2, 7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8, 2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6,
              11]
    S_BOX = [S1_BOX, S2_BOX, S3_BOX, S4_BOX, S5_BOX, S6_BOX, S7_BOX, S8_BOX]
    P_BOX = [16, 7, 20, 21, 29, 12, 28, 17, 1, 15, 23, 26, 5, 18, 31, 10, 2, 8, 24, 14, 32, 27, 3, 9, 19, 13, 30, 6, 22,
             11, 4, 25]
    IP_BOX = [58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4, 62, 54, 46, 38, 30, 22, 14, 6, 64, 56, 48,
              40, 32, 24, 16, 8, 57, 49, 41, 33, 25, 17, 9, 1, 59, 51, 43, 35, 27, 19, 11, 3, 61, 53, 45, 37, 29, 21,
              13, 5, 63, 55, 47, 39, 31, 23, 15, 7]
    IP_1_BOX = [40, 8, 48, 16, 56, 24, 64, 32, 39, 7, 47, 15, 55, 23, 63, 31, 38, 6, 46, 14, 54, 22, 62, 30, 37, 5, 45,
                13, 53, 21, 61, 29, 36, 4, 44, 12, 52, 20, 60, 28, 35, 3, 43, 11, 51, 19, 59, 27, 34, 2, 42, 10, 50, 18,
                58, 26, 33, 1, 41, 9, 49, 17, 57, 25]

    @staticmethod
    def encode(plaintext: str, key_hex: str):
        child_keys = DES.devire_key(DES.hextobin(key_hex))
        pt_64bit = DES.ip(DES.hextobin(plaintext))
        pltext_l, pltext_r = pt_64bit[:64 // 2], pt_64bit[64 // 2:]
        for i in range(16):
            pltext_l, pltext_r = DES.cal(pltext_l, pltext_r, child_keys[i])
        ciphertext = DES.fp(pltext_r + pltext_l)
        return DES.bintohex(ciphertext)

    @staticmethod
    def decode(ciphertext: str, key: str):
        child_key = DES.devire_key(DES.hextobin(key))
        cp_64bit = DES.ip(DES.hextobin(ciphertext))
        ciptext, ciptext_l = cp_64bit[:64 // 2], cp_64bit[64 // 2:]

        for i in range(15, -1, -1):
            ciptext, ciptext_l = DES.cal(ciptext, ciptext_l, child_key[i])

        plaintext = DES.fp(ciptext_l + ciptext)

        return DES.bintohex(plaintext)

    @staticmethod
    def devire_key(key_bin: str):
        key0 = ""
        for i in DES.PC_1:
            key0 += key_bin[i - 1]
        key_c, key_d = key0[:56 // 2], key0[56 // 2:]

        def shift_left(text, n):
            return text[DES.Lap[n]:] + text[:DES.Lap[n]]

        sub_k = []
        for i in range(16):
            key_c = shift_left(key_c, i)
            key_d = shift_left(key_d, i)
            temp = key_c + key_d
            k = ""
            for j in DES.PC_2:
                k += temp[j - 1]
            sub_k.append(k)
        return sub_k

    @staticmethod
    def func_f(r: str, k: str):
        expend = ""
        for i in DES.E_BOX:
            expend += r[i - 1]

        xor = bin(int(expend, 2) ^ int(k, 2))[2:].zfill(len(k))
        start = 0
        s = ""
        for i in range(8):
            b = xor[start:start + 6]
            r = int(b[0] + b[5], 2)
            c = int(b[1: 5], 2)
            s += bin(DES.S_BOX[i][r * 16 + c])[2:].zfill(4)
            start += 6
        f = ""
        for i in DES.P_BOX:
            f += s[i - 1]
        return f

    @staticmethod
    def cal(left: str, right: str, k: str):
        r_res = bin(int(left, 2) ^ int(DES.func_f(right, k), 2))[2:].zfill(len(left))
        l_res = right
        return l_res, r_res

    @staticmethod
    def ip(plaintext: str):
        res = ""
        for i in DES.IP_BOX:
            res += plaintext[i - 1]
        return res

    @staticmethod
    def fp(plaintext: str):
        text = plaintext.zfill(64)
        res = ""
        for i in DES.IP_1_BOX:
            res += text[i - 1]
        return res

    @staticmethod
    def hextobin(num_hex: str):
        num_bin = bin(int(num_hex, 16))[2:].zfill(64)
        return num_bin

    @staticmethod
    def bintohex(num_bin: str):
        num_hex = hex(int(num_bin, 2))[2:].upper().zfill(16)
        return num_hex


class AES:
    _index = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        'A': 10,
        'B': 11,
        'C': 12,
        'D': 13,
        'E': 14,
        'F': 15,
        'a': 10,
        'b': 11,
        'c': 12,
        'd': 13,
        'e': 14,
        'f': 15
    }
    s_box = [
        ['63', '7C', '77', '7B', 'F2', '6B', '6F', 'C5', '30', '01', '67', '2B', 'FE', 'D7', 'AB', '76'],
        ['CA', '82', 'C9', '7D', 'FA', '59', '47', 'F0', 'AD', 'D4', 'A2', 'AF', '9C', 'A4', '72', 'C0'],
        ['B7', 'FD', '93', '26', '36', '3F', 'F7', 'CC', '34', 'A5', 'E5', 'F1', '71', 'D8', '31', '15'],
        ['04', 'C7', '23', 'C3', '18', '96', '05', '9A', '07', '12', '80', 'E2', 'EB', '27', 'B2', '75'],
        ['09', '83', '2C', '1A', '1B', '6E', '5A', 'A0', '52', '3B', 'D6', 'B3', '29', 'E3', '2F', '84'],
        ['53', 'D1', '00', 'ED', '20', 'FC', 'B1', '5B', '6A', 'CB', 'BE', '39', '4A', '4C', '58', 'CF'],
        ['D0', 'EF', 'AA', 'FB', '43', '4D', '33', '85', '45', 'F9', '02', '7F', '50', '3C', '9F', 'A8'],
        ['51', 'A3', '40', '8F', '92', '9D', '38', 'F5', 'BC', 'B6', 'DA', '21', '10', 'FF', 'F3', 'D2'],
        ['CD', '0C', '13', 'EC', '5F', '97', '44', '17', 'C4', 'A7', '7E', '3D', '64', '5D', '19', '73'],
        ['60', '81', '4F', 'DC', '22', '2A', '90', '88', '46', 'EE', 'B8', '14', 'DE', '5E', '0B', 'DB'],
        ['E0', '32', '3A', '0A', '49', '06', '24', '5C', 'C2', 'D3', 'AC', '62', '91', '95', 'E4', '79'],
        ['E7', 'C8', '37', '6D', '8D', 'D5', '4E', 'A9', '6C', '56', 'F4', 'EA', '65', '7A', 'AE', '08'],
        ['BA', '78', '25', '2E', '1C', 'A6', 'B4', 'C6', 'E8', 'DD', '74', '1F', '4B', 'BD', '8B', '8A'],
        ['70', '3E', 'B5', '66', '48', '03', 'F6', '0E', '61', '35', '57', 'B9', '86', 'C1', '1D', '9E'],
        ['E1', 'F8', '98', '11', '69', 'D9', '8E', '94', '9B', '1E', '87', 'E9', 'CE', '55', '28', 'DF'],
        ['8C', 'A1', '89', '0D', 'BF', 'E6', '42', '68', '41', '99', '2D', '0F', 'B0', '54', 'BB', '16']
    ]
    inv_s_box = [
        ['52', '09', '6A', 'D5', '30', '36', 'A5', '38', 'BF', '40', 'A3', '9E', '81', 'F3', 'D7', 'FB'],
        ['7C', 'E3', '39', '82', '9B', '2F', 'FF', '87', '34', '8E', '43', '44', 'C4', 'DE', 'E9', 'CB'],
        ['54', '7B', '94', '32', 'A6', 'C2', '23', '3D', 'EE', '4C', '95', '0B', '42', 'FA', 'C3', '4E'],
        ['08', '2E', 'A1', '66', '28', 'D9', '24', 'B2', '76', '5B', 'A2', '49', '6D', '8B', 'D1', '25'],
        ['72', 'F8', 'F6', '64', '86', '68', '98', '16', 'D4', 'A4', '5C', 'CC', '5D', '65', 'B6', '92'],
        ['6C', '70', '48', '50', 'FD', 'ED', 'B9', 'DA', '5E', '15', '46', '57', 'A7', '8D', '9D', '84'],
        ['90', 'D8', 'AB', '00', '8C', 'BC', 'D3', '0A', 'F7', 'E4', '58', '05', 'B8', 'B3', '45', '06'],
        ['D0', '2C', '1E', '8F', 'CA', '3F', '0F', '02', 'C1', 'AF', 'BD', '03', '01', '13', '8A', '6B'],
        ['3A', '91', '11', '41', '4F', '67', 'DC', 'EA', '97', 'F2', 'CF', 'CE', 'F0', 'B4', 'E6', '73'],
        ['96', 'AC', '74', '22', 'E7', 'AD', '35', '85', 'E2', 'F9', '37', 'E8', '1C', '75', 'DF', '6E'],
        ['47', 'F1', '1A', '71', '1D', '29', 'C5', '89', '6F', 'B7', '62', '0E', 'AA', '18', 'BE', '1B'],
        ['FC', '56', '3E', '4B', 'C6', 'D2', '79', '20', '9A', 'DB', 'C0', 'FE', '78', 'CD', '5A', 'F4'],
        ['1F', 'DD', 'A8', '33', '88', '07', 'C7', '31', 'B1', '12', '10', '59', '27', '80', 'EC', '5F'],
        ['60', '51', '7F', 'A9', '19', 'B5', '4A', '0D', '2D', 'E5', '7A', '9F', '93', 'C9', '9C', 'EF'],
        ['A0', 'E0', '3B', '4D', 'AE', '2A', 'F5', 'B0', 'C8', 'EB', 'BB', '3C', '83', '53', '99', '61'],
        ['17', '2B', '04', '7E', 'BA', '77', 'D6', '26', 'E1', '69', '14', '63', '55', '21', '0C', '7D'],
    ]
    c_matrix = [
        ['02', '03', '01', '01'],
        ['01', '02', '03', '01'],
        ['01', '01', '02', '03'],
        ['03', '01', '01', '02']
    ]
    c_1_matrix = [
        ['0E', '0B', '0D', '09'],
        ['09', '0E', '0B', '0D'],
        ['0D', '09', '0E', '0B'],
        ['0B', '0D', '09', '0E']
    ]
    rcon = [
        ['01', '00', '00', '00'], ['02', '00', '00', '00'],
        ['04', '00', '00', '00'], ['08', '00', '00', '00'],
        ['10', '00', '00', '00'], ['20', '00', '00', '00'],
        ['40', '00', '00', '00'], ['80', '00', '00', '00'],
        ['1b', '00', '00', '00'], ['36', '00', '00', '00']
    ]

    @staticmethod
    def keyexpansion(key):
        def xor(a, b):
            r = []
            for i in range(4):
                na = int(a[i], 16)
                nb = int(b[i], 16)
                r.append(hex(na ^ nb)[2:].upper().zfill(2))
            return r

        w = [[] for _ in range(44)]
        matrix_w = []
        for i in range(4):
            t = key[i * 8:i * 8 + 8]
            w[i] = [t[:2], t[2:4], t[4:6], t[6:8]]
        for i in range(4, 44):
            if i % 4 != 0:
                w[i] = xor(w[i - 1], w[i - 4])
            else:
                rot = AES.rotword(w[i - 1])
                sub = AES.subword(rot)
                temp = xor(sub, b=AES.rcon[i // 4 - 1])
                w[i] = xor(temp, w[i - 4])

        for i in range(0, 44, 4):
            row = []
            for j in range(4):
                row.append(w[i + j])
            matrix_w.append(row)
        return matrix_w

    @staticmethod
    def addroundkey(matrix, key):
        res = []
        for i in range(4):
            row = []
            for j in range(4):
                row.append(hex(int(matrix[i][j], 16) ^ int(key[i][j], 16))[2:].upper().zfill(2))
            res.append(row)
        return res

    @staticmethod
    def subbytes(matrix: list):
        res = []
        for v in matrix:
            row = []
            for i in v:
                x = AES._index[i[0]]
                y = AES._index[i[1]]
                row.append(AES.s_box[x][y].zfill(2))
            res.append(row)
        return res

    @staticmethod
    def shiftrows(matrix: list):
        shift = 0
        res = matrix.copy()
        for i in range(4):
            col = []
            for j in range(4):
                col.append(matrix[j][i])
            j = 0
            for k in col[shift:] + col[:shift]:
                res[j][i] = k
                j += 1
            shift += 1
        return res

    @staticmethod
    def mixcolumns(matrix: list):
        res = []
        for i in range(4):
            row = []
            for j in range(4):
                flag = True
                cell = 0
                for k in range(4):
                    if flag:
                        cell = AES.galois_mult(AES.c_matrix[i][k], matrix[j][k])
                        flag = False
                    else:
                        cell ^= AES.galois_mult(AES.c_matrix[i][k], matrix[j][k])
                row.append(hex(cell)[2:].upper().zfill(2))
            res.append(row)
        res = AES.rotate(res)

        return res

    @staticmethod
    def invsubbytes(matrix: list):
        res = []
        for v in matrix:
            row = []
            for i in v:
                x = AES._index[i[0]]
                y = AES._index[i[1]]
                row.append(AES.inv_s_box[x][y].zfill(2))
            res.append(row)
        return res

    @staticmethod
    def invshiftrows(matrix: list):
        shift = 4
        res = matrix.copy()
        for i in range(4):
            col = []
            for j in range(4):
                col.append(matrix[j][i])
            j = 0
            for k in col[shift:] + col[:shift]:
                res[j][i] = k
                j += 1
            shift -= 1
        return res

    @staticmethod
    def invmixcolumns(matrix: list):
        res = []
        for i in range(4):
            row = []
            for j in range(4):
                flag = True
                cell = 0
                for k in range(4):
                    if flag:
                        cell = AES.galois_mult(AES.c_1_matrix[i][k], matrix[j][k])
                        flag = False
                    else:
                        cell ^= AES.galois_mult(AES.c_1_matrix[i][k], matrix[j][k])
                row.append(hex(cell)[2:].upper().zfill(2))
            res.append(row)
        res = AES.rotate(res)
        return res

    @staticmethod
    def rotword(word):
        r = word[1:] + word[:1]
        return r

    @staticmethod
    def subword(word: str):
        r = []
        for i in word:
            x = AES._index[i[0]]
            y = AES._index[i[1]]
            r.append(AES.s_box[x][y])
        return r

    @staticmethod
    def rotate(matrix):
        length = len(matrix)
        for i in range(length):
            for j in range(i, length):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        return matrix

    @staticmethod
    def galois_mult(num_a, num_b):
        a = int(num_a, 16)
        b = int(num_b, 16)
        p = 0

        for i in range(8):
            b_1 = b & 1
            if b_1 == 1:
                p ^= a
            hi_bit_set = a & 0x80
            a <<= 1
            if hi_bit_set == 0x80:
                a ^= 0x1b
            b >>= 1

        return p % 256

    @staticmethod
    def encode(plaintext: str, key: str):
        state = AES.trans_matrix(plaintext)
        matrix_w = AES.keyexpansion(key)
        res = state
        res = AES.addroundkey(res, matrix_w[0])
        for i in range(1, 10):
            res = AES.subbytes(res)
            res = AES.shiftrows(res)
            res = AES.mixcolumns(res)
            res = AES.addroundkey(res, matrix_w[i])

        res = AES.subbytes(res)
        res = AES.shiftrows(res)
        res = AES.addroundkey(res, matrix_w[10])
        return AES.trans_text(res)

    @staticmethod
    def decode(ciphertext: str, key: str):
        state = AES.trans_matrix(ciphertext)

        matrix_w = AES.keyexpansion(key)
        res = state
        res = AES.addroundkey(res, matrix_w[10])
        for i in range(9, 0, -1):
            res = AES.invshiftrows(res)
            res = AES.invsubbytes(res)
            res = AES.addroundkey(res, matrix_w[i])
            res = AES.invmixcolumns(res)

        res = AES.invshiftrows(res)
        res = AES.invsubbytes(res)
        res = AES.addroundkey(res, matrix_w[0])
        return AES.trans_text(res)

    @staticmethod
    def trans_matrix(text: str):
        matrix = []
        index = 0
        for i in range(4):
            row = []
            for j in range(4):
                row.append(text[index:index + 2].zfill(2))
                index += 2
            matrix.append(row)
        return matrix

    @staticmethod
    def trans_text(matrix: list):
        text = ''
        for i in matrix:
            for j in i:
                text += j
        return text
