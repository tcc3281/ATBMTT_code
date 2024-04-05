import string


class Cryptology:
    _uppercase = list(string.ascii_uppercase)
    _lowercase = list(string.ascii_lowercase)

    @staticmethod
    def _simple(text: str) -> str:
        return text.replace(" ", "").lower()

    @staticmethod
    def _getindex(word: chr) -> int:
        return ord(word) - ord('a')

    @staticmethod
    def _creatematrixplayfair(key: str) -> [int]:
        had = set()
        matrix = []
        for i in (key + string.ascii_lowercase).replace('j', 'i'):
            if i not in had:
                matrix.append(i)
                had.add(i)
        return matrix

    @staticmethod
    def _addword(word: chr, num: int) -> chr:
        mod = 26
        res = (ord(word) - ord('a')) + num
        res %= mod
        res += ord('a')
        return chr(res)

    @staticmethod
    def _minusword(word: chr, num: int) -> chr:
        mod = 26
        res = (ord(word) - ord('a')) - num
        res %= mod
        res += ord('a')
        return chr(res)

    @staticmethod
    def encodeceasar(plaintext: str, key: int) -> str:
        plaintext = Cryptology._simple(plaintext)
        ciphertext = ""
        for i in plaintext:
            if 'a' <= i <= 'z':
                ciphertext += Cryptology._addword(i, key)
        return ciphertext

    @staticmethod
    def decodeceasar(ciphertext: str, key: int) -> str:
        ciphertext = Cryptology._simple(ciphertext)
        plaintext = ""
        for i in ciphertext:
            if 'a' <= i <= 'z':
                plaintext += Cryptology._minusword(i, key)
        return plaintext

    @staticmethod
    def encodeplayfair(plaintext: str, key: str) -> str:
        plaintext = Cryptology._simple(plaintext).replace("j", "i")
        key = Cryptology._simple(key)
        cryt = []
        i, n = 0, len(plaintext)
        while i < n:
            if i == n - 1:
                cryt.append(plaintext[i] + 'x')
            elif plaintext[i] == plaintext[i + 1]:
                cryt.append(plaintext[i] + 'x')
                i -= 1
            else:
                cryt.append(plaintext[i:i + 2])
            i += 2
        matrix = Cryptology._creatematrixplayfair(key)
        ciphertext = ""

        for a, b in cryt:
            pa = matrix.index(a)
            pb = matrix.index(b)
            ia, ja = pa // 5, pa % 5
            ib, jb = pb // 5, pb % 5
            if ja == jb:
                ciphertext += (matrix[int(((ia + 1) % 5) * 5 + ja)] + matrix[int(((ib + 1) % 5) * 5 + jb)])
            elif ia == ib:
                ciphertext += (matrix[int(ia * 5 + ((ja + 1) % 5))] + matrix[int(ib * 5 + ((jb + 1) % 5))])
            else:
                ciphertext += (matrix[int(ia * 5 + jb)] + matrix[int(ib * 5 + ja)])
        return ciphertext

    @staticmethod
    def decodeplayfair(ciphertext, key):
        ciphertext = Cryptology._simple(ciphertext).replace("j", "i")
        key = Cryptology._simple(key)
        cryt = []
        i, n = 0, len(ciphertext)
        while i < n:
            if i == n - 1:
                cryt.append(ciphertext[i] + 'x')
            elif ciphertext[i] == ciphertext[i + 1]:
                cryt.append(ciphertext[i] + 'x')
                i -= 1
            else:
                cryt.append(ciphertext[i:i + 2])
            i += 2
        matrix = Cryptology._creatematrixplayfair(key)
        plaintext = ""
        for a, b in cryt:
            pa = matrix.index(a)
            pb = matrix.index(b)
            ia, ja = pa // 5, pa % 5
            ib, jb = pb // 5, pb % 5
            if ja == jb:
                plaintext += (matrix[int(((ia - 1) % 5) * 5 + ja)] + matrix[int(((ib - 1) % 5) * 5 + jb)])
            elif ia == ib:
                plaintext += (matrix[int(ia * 5 + ((ja - 1) % 5))] + matrix[int(ib * 5 + ((jb - 1) % 5))])
            else:
                plaintext += (matrix[int(ia * 5 + jb)] + matrix[int(ib * 5 + ja)])
        return plaintext

    @staticmethod
    def encodevigenere(plaintext: str, key: str) -> str:
        plaintext = Cryptology._simple(plaintext)
        key = Cryptology._simple(key)
        l_key = len(key)
        index = 0
        ciphertext = ""
        for i in plaintext:
            if "a" <= i <= "z":
                ciphertext += Cryptology._addword(i, Cryptology._getindex(key[index]))
                index = (index + 1) % l_key
        return ciphertext

    @staticmethod
    def decodevigenere(ciphertext: str, key: str) -> str:
        ciphertext = Cryptology._simple(ciphertext)
        key = Cryptology._simple(key)
        l_key = len(key)
        key = key.lower()
        index = 0
        ciphertext = ciphertext.lower().replace(" ", "")
        plaintext = ""
        for i in ciphertext:
            if "a" <= i <= "z":
                plaintext += Cryptology._minusword(i, Cryptology._getindex(key[index]))
                index = (index + 1) % l_key
        return plaintext

    @staticmethod
    def encodeautokey(plaintext: str, key: str) -> str:
        key = Cryptology._simple(key)
        plaintext = Cryptology._simple(plaintext)
        key = (key + plaintext).lower()
        ciphertext = ""
        index = 0
        for i in plaintext:
            if "a" <= i <= "z":
                ciphertext += Cryptology._addword(i, Cryptology._getindex(key[index]))
                index += 1
        return ciphertext

    @staticmethod
    def decodeautokey(ciphertext: str, key: str) -> str:
        key = Cryptology._simple(key)
        ciphertext = Cryptology._simple(ciphertext)
        l_key = len(key)
        temp_key = key
        plaintext = ""
        start_index = 0
        index = 0
        for i in ciphertext:
            if "a" <= i <= "z":
                plaintext += Cryptology._minusword(i, Cryptology._getindex(temp_key[index]))
                index += 1
                if index == l_key:
                    index = 0
                    temp_key = plaintext[start_index:start_index + l_key]
                    start_index += l_key
        return plaintext

    @staticmethod
    def encodemonographic(plaintext: str, key: str) -> str:
        key = Cryptology._simple(key)
        plaintext = Cryptology._simple(plaintext)
        dic = dict(zip(Cryptology._lowercase, key))
        ciphertext = ""
        for i in plaintext:
            ciphertext += dic[i]
        return ciphertext

    @staticmethod
    def decodemonographic(ciphertext: str, key: str) -> str:
        key = Cryptology._simple(key)
        ciphertext = Cryptology._simple(ciphertext)
        dic = dict(zip(key, Cryptology._lowercase))
        plaintext = ""
        for i in ciphertext:
            plaintext += dic[i]
        return plaintext

    @staticmethod
    def encoderailfence(plaintext: str, key: int) -> str:
        key = int(key)
        plaintext = Cryptology._simple(plaintext)
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
    def rota(a):
        b = [list(reversed(x)) for x in zip(*a)]
        return b

    @staticmethod
    def decoderailfence(ciphertext: str, key: int) -> str:
        ciphertext = Cryptology._simple(ciphertext)
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
        print(*matrix, sep="\n")
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

    @staticmethod
    def encodetransposition(plaintext: str, key: str) -> str:
        plaintext = Cryptology._simple(plaintext)
        dic = dict(zip(list(map(int, str(key))), list(map(int, sorted(str(key))))))
        m = len(str(key))
        l_p = len(plaintext)
        if l_p % m != 0:
            k = ((l_p // m) + 1) * m - l_p
            plaintext = plaintext + string.ascii_lowercase[26 - k:26]
        matrix = [[] for _ in range(m)]
        index = 0
        for i in plaintext:
            matrix[index].append(i)
            index = (index + 1) % m
        ciphertext = ""
        for i in range(1, m + 1):
            for j in matrix[dic[i] - 1]:
                ciphertext += j
        return ciphertext

    @staticmethod
    def decodetransposition(ciphertext: str, key: str) -> str:
        ciphertext = Cryptology._simple(ciphertext)
        dic = dict(zip(list(map(int, str(key))), list(map(int, sorted(str(key))))))
        l_key = str(key)
        m = len(l_key)
        matrix = [[] for _ in range(m)]
        max_length = len(ciphertext) // m
        cur = 0
        for i, v in enumerate(ciphertext):
            if i % max_length == 0:
                cur += 1
            matrix[dic[cur] - 1].append(v)
        plaintext = ""
        for i in range(len(matrix[0])):
            for j in range(m):
                plaintext += matrix[j][i]
        return plaintext
