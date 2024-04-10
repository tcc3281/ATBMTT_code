import string


class Cryptology:
    _uppercase = list(string.ascii_uppercase)
    _lowercase = list(string.ascii_lowercase)

    @staticmethod
    def encode_ceasar(plaintext: str, key: int):
        res = ''
        for i in plaintext:
            if i in Cryptology._uppercase:
                res += Cryptology._uppercase[(Cryptology._uppercase.index(i) + key) % 26]
            elif i in Cryptology._lowercase:
                res += Cryptology._lowercase[(Cryptology._lowercase.index(i) + key) % 26]
            else:
                res += i
        return res

    @staticmethod
    def decode_ceasar(ciphertext: str, key: int):
        res = ''
        for i in ciphertext:
            if i in Cryptology._uppercase:
                res += Cryptology._uppercase[(Cryptology._uppercase.index(i) - key) % 26]
            elif i in Cryptology._lowercase:
                res += Cryptology._lowercase[(Cryptology._lowercase.index(i) - key) % 26]
            else:
                res += i
        return res

    @staticmethod
    def encode_vingenere(plaintext: str, key: str):
        ciphertext = ''
        for i in range(len(plaintext)):
            if plaintext[i] in Cryptology._uppercase:
                ciphertext += Cryptology._uppercase[
                    (Cryptology._uppercase.index(plaintext[i]) + Cryptology._uppercase.index(key[i % len(key)])) % 26]
            elif plaintext[i] in Cryptology._lowercase:
                ciphertext += Cryptology._lowercase[
                    (Cryptology._lowercase.index(plaintext[i]) + Cryptology._lowercase.index(key[i % len(key)])) % 26]
            else:
                ciphertext += plaintext[i]
        return ciphertext

    @staticmethod
    def decode_vingenere(ciphertext: str, key: str):
        plaintext = ''
        for i in range(len(ciphertext)):
            if ciphertext[i] in Cryptology._uppercase:
                plaintext += Cryptology._uppercase[
                    (Cryptology._uppercase.index(ciphertext[i]) - Cryptology._uppercase.index(key[i % len(key)])) % 26]
            elif ciphertext[i] in Cryptology._lowercase:
                plaintext += Cryptology._lowercase[
                    (Cryptology._lowercase.index(ciphertext[i]) - Cryptology._lowercase.index(key[i % len(key)])) % 26]
            else:
                plaintext += ciphertext[i]
        return plaintext

    @staticmethod
    def encode_autokey(plaintext: str, key: str):
        ciphertext = ''
        length = len(key)
        for i in range(len(plaintext)):
            if i != 0 and i % length == 0:
                key += plaintext[i - length:i]
            ciphertext += Cryptology.encode_ceasar(plaintext[i], Cryptology._uppercase.index(key[i]))
        return ciphertext

    @staticmethod
    def decode_autokey(ciphertext: str, key: str):
        plaintext = ''
        length = len(key)
        for i in range(len(ciphertext)):
            if i != 0 and i % length == 0:
                key += plaintext[i - length:i]
            plaintext += Cryptology.decode_ceasar(ciphertext[i], Cryptology._uppercase.index(key[i]))
        return plaintext

    @staticmethod
    def encode_monographic(plaintext: str, key: str):
        ciphertext = ''
        dict_key = dict(zip(Cryptology._uppercase, key))
        for i in plaintext:
            if i in Cryptology._uppercase:
                ciphertext += dict_key[i]
            else:
                ciphertext += i
        return ciphertext

    @staticmethod
    def decode_monographic(ciphertext: str, key: str):
        plaintext = ''
        dict_key = dict(zip(key, Cryptology._uppercase))
        for i in ciphertext:
            if i in Cryptology._uppercase:
                plaintext += dict_key[i]
            else:
                plaintext += i
        return plaintext

    @staticmethod
    def create_matrix_playfair(key: str):
        matrix = []
        for i in key:
            if i not in matrix:
                matrix.append(i)
        for i in Cryptology._uppercase:
            if i == 'J':
                continue
            if i not in key:
                matrix.append(i)
        return matrix

    @staticmethod
    def __get_pos_mtplayfair(position):
        x = position // 5
        y = position % 5

        return [x, y]
    @staticmethod
    def __get_pos_arrayplayfair(x, y):
        return x * 5 + y

    @staticmethod
    def encode_playfair(plaintext: str, key: str):
        matrix = Cryptology.create_matrix_playfair(key)
        ciphertext = ''
        p = plaintext.replace(' ', '')
        split_text = []
        length = len(p)
        step = 0
        while step < length:
            try:
                if p[step] != p[step + 1]:
                    split_text.append(p[step:step + 2])
                else:
                    split_text.append(p[step] + 'X')
                    step = step - 1
            except:
                split_text.append(p[step] + 'Z')
            finally:
                step += 2

        for v in split_text:
            index = Cryptology.__get_pos_mtplayfair(matrix.index(v[0])) + Cryptology.__get_pos_mtplayfair(
                matrix.index(v[1]))
            if index[0] == index[2]:
                ciphertext += matrix[Cryptology.__get_pos_arrayplayfair(index[0],(index[1]+1)%5)] + matrix[Cryptology.__get_pos_arrayplayfair(index[2],(index[3]+1)%5)]
            elif index[1] == index[3]:
                ciphertext += matrix[Cryptology.__get_pos_arrayplayfair((index[0]+1)%5,index[1])] + matrix[Cryptology.__get_pos_arrayplayfair((index[2]+1)%5,index[3])]
            else:
                ciphertext += matrix[Cryptology.__get_pos_arrayplayfair(index[0],index[3])] + matrix[Cryptology.__get_pos_arrayplayfair(index[2],index[1])]
        return ciphertext

    @staticmethod
    def decode_playfair(ciphertext :str, key:str):
        matrix = Cryptology.create_matrix_playfair(key)
        plaintext = ''
        p = ciphertext.replace(' ', '')
        split_text = []
        length = len(p)
        step = 0
        while step < length:
            try:
                if p[step] != p[step + 1]:
                    split_text.append(p[step:step + 2])
                else:
                    split_text.append(p[step] + 'X')
                    step = step - 1
            except:
                split_text.append(p[step] + 'Z')
            finally:
                step += 2

        for v in split_text:
            index = Cryptology.__get_pos_mtplayfair(matrix.index(v[0])) + Cryptology.__get_pos_mtplayfair(
                matrix.index(v[1]))
            if index[0] == index[2]:
                plaintext += matrix[Cryptology.__get_pos_arrayplayfair(index[0], (index[1] - 1) % 5)] + matrix[
                    Cryptology.__get_pos_arrayplayfair(index[2], (index[3] - 1) % 5)]
            elif index[1] == index[3]:
                plaintext += matrix[Cryptology.__get_pos_arrayplayfair((index[0] - 1) % 5, index[1])] + matrix[
                    Cryptology.__get_pos_arrayplayfair((index[2] - 1) % 5, index[3])]
            else:
                plaintext += matrix[Cryptology.__get_pos_arrayplayfair(index[0], index[3])] + matrix[
                    Cryptology.__get_pos_arrayplayfair(index[2], index[1])]
        return plaintext

    @staticmethod
    def __rota(a):
        b = [list(reversed(x)) for x in zip(*a)]
        return b

    @staticmethod
    def encoderailfence(plaintext: str, key: int) -> str:
        key = int(key)
        matrix = []
        index = 0
        step = 1
        for i in plaintext:
            mt = [''] * key
            mt[index] = i
            matrix.append(mt)
            if index + step == -1 or index + step == key:
                step *= -1
            index += step
        m = len(matrix)
        n = len(matrix[0])
        ciphertext = ""
        for i in range(n):
            for j in range(m):
                if matrix[j][i] != '':
                    ciphertext += matrix[j][i]

        return ciphertext


    @staticmethod
    def decoderailfence(ciphertext: str, key: int) -> str:
        matrix = []
        index = 0
        step = 1
        for i in ciphertext:
            mt = [''] * key
            mt[index] = i
            matrix.append(mt)
            if index + step == -1 or index + step == key:
                step *= -1
                index += step
            else:
                index += step
        m = len(matrix)
        n = len(matrix[0])
        index = 0
        for i in range(n):
            for j in range(m):
                if matrix[j][i] != '':
                    matrix[j][i] = ciphertext[index]
                    index += 1
        plaintext = ""
        for i in matrix:
            for j in i:
                if j != '':
                    plaintext += j
        return plaintext


def ceasar():
    plaintext = 'STILLWATERSRUNDE'
    key = 3
    ciphertext = Cryptology.encode_ceasar(plaintext, key)
    print("Ceasar:")
    print("Ciphertext:", ciphertext)
    print("Plaintext:", Cryptology.decode_ceasar(ciphertext, key))


def vingenere():
    plaintext = 'THETRUTHWILLO'
    key = 'THEGRASS'
    ciphertext = Cryptology.encode_vingenere(plaintext, key)
    print("Vingernere:")
    print("Ciphertext:", ciphertext)
    print("Plaintext:", Cryptology.decode_vingenere(ciphertext, key))


def autokey():
    plaintext = 'THETRUTHWILLO'
    key = 'THEGRASS'
    ciphertext = Cryptology.encode_autokey(plaintext, key)
    print("Autokey:")
    print("Ciphertext:", ciphertext)
    print("Plaintext:", Cryptology.decode_autokey(ciphertext, key))


def monographic():
    plaintext = 'MONEYMAKESTHEMAR'
    key = 'JEHFAVZNOXUBMYPKDLGSRCTWQI'
    ciphertext = Cryptology.encode_monographic(plaintext, key)
    print("Monographic:")
    print("Ciphertext:", ciphertext)
    print("Plaintext:", Cryptology.decode_monographic(ciphertext, key))

def playfair():
    plaintext = 'ACLEANFASTISB'
    key = 'EASTO'
    ciphertext = Cryptology.encode_playfair(plaintext, key)
    print("Playfair:")
    print("Ciphertext:", ciphertext)
    print("Plaintext:", Cryptology.decode_playfair(ciphertext, key))

def railfence():
    plaintext = 'STILLWATERSRUNDE'
    key = 3
    ciphertext = Cryptology.encoderailfence(plaintext, key)
    print("Railfence:")
    print("Ciphertext:", ciphertext)
    print("Plaintext:", Cryptology.decoderailfence(ciphertext, key))
if __name__ == '__main__':
    ceasar()
    vingenere()
    autokey()
    monographic()
    playfair()
    railfence()