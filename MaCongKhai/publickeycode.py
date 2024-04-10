class RSA:
    def __init__(self, p, q, e=65537):
        self.p = p
        self.q = q
        self.n = p * q
        self.phi = (p - 1) * (q - 1)
        self.e = e
        self.d = self.modinv(self.e, self.phi)

    def modinv(self, a, m):
        m0, x0, x1 = m, 0, 1
        while a > 1:
            q = a // m
            m, a = a % m, m
            x0, x1 = x1 - q * x0, x0
        return x1 + m0 if x1 < 0 else x1

    def encrypt(self, plaintext):
        return pow(plaintext, self.e, self.n)

    def decrypt(self, ciphertext):
        return pow(ciphertext, self.d, self.n)

    def encrypt_string(self, plaintext):
        return [self.encrypt(ord(char)) for char in plaintext]

    def decrypt_string(self, ciphertext):
        return ''.join([chr(self.decrypt(char)) for char in ciphertext])

    def get_public_key(self):
        return self.e, self.n

    def get_private_key(self):
        return self.d, self.n

class DiffieHellman:
    def __init__(self, p, g):
        self.p = p
        self.g = g

    def generate_key(self, private_key):
        return pow(self.g, private_key, self.p)

    def generate_shared_secret(self, private_key, public_key):
        return pow(public_key, private_key, self.p)

class ElGamal:
    def __init__(self, p, g, x):
        self.p = p
        self.g = g
        self.x = x
        self.y = pow(self.g, self.x, self.p)

    def encrypt(self, M, k):
        a = pow(self.g, k, self.p)
        b = (M *pow(self.get_public_key(), k, self.p))% self.p
        return a, b

    def decrypt(self, ciphertext):
        a, b = ciphertext
        return (b * pow(a, self.p - 1 - self.x, self.p)) % self.p

    def get_public_key(self):
        return self.y

    def get_private_key(self):
        return self.x

    def sign(self, M):
        k = 5
        r = pow(self.g, k, self.p)
        s = (M - self.x * r) * self.modinv(k, self.p - 1) % (self.p - 1)
        return r, s

    def verify(self, M, signature, public_key):
        r, s = signature
        y = public_key
        if 1 <= r <= self.p - 1 and 1 <= s <= self.p - 1:
            w = self.modinv(s, self.p - 1)
            u1 = (M * w) % (self.p - 1)
            u2 = (r * w) % (self.p - 1)
            v = ((pow(self.g, u1, self.p) * pow(y, u2, self.p)) % self.p) % (self.p - 1)
            return v == r
        return False

    def modinv(self, a, m):
        m0, x0, x1 = m, 0, 1
        while a > 1:
            q = a // m
            m, a = a % m, m
            x0, x1 = x1 - q * x0, x0
        return x1 + m0 if x1 < 0 else x1

class DSA:
    def __init__(self, p, q, g, x):
        self.p = p
        self.q = q
        self.g = g
        self.x = x
        self.y = pow(self.g, self.x, self.p)

    def get_public_key(self):
        return self.y

    def sign(self, M, k):
        r = pow(self.g, k, self.p) % self.q
        s = (pow(k, self.q - 2, self.q) * (M + self.x * r)) % self.q
        return r, s

    def verify(self, M, signature):
        r, s = signature
        w = pow(s, self.q - 2, self.q)
        u1 = (M * w) % self.q
        u2 = (r * w) % self.q
        v = ((pow(self.g, u1, self.p) * pow(self.y, u2, self.p)) % self.p) % self.q
        return v == r

    def modinv(self, a, m):
        m0, x0, x1 = m, 0, 1
        while a > 1:
            q = a // m
            m, a = a % m, m
            x0, x1 = x1 - q * x0, x0
        return x1 + m0 if x1 < 0 else x1

def rsa():
    rsa = RSA(31, 47, 43)
    M = 53
    print('Public key:', rsa.get_public_key())
    print('Private key:', rsa.get_private_key())
    print('Plaintext:', M)
    print('Encrypted:', rsa.encrypt(M))

def diffie_hellman():
    dh = DiffieHellman(7207, 3)
    an_private_key = 422
    ba_private_key = 286
    an_public_key = dh.generate_key(an_private_key)
    ba_public_key = dh.generate_key(ba_private_key)
    shared_secret = dh.generate_shared_secret(an_private_key, ba_public_key)
    print('Alice public key:', an_public_key)
    print('Bob public key:', ba_public_key)
    print('Shared secret:', shared_secret)

def elgamal():
    elgamal = ElGamal(7349, 3, 366)
    M = 333
    k = 32
    print('Public key:', elgamal.get_public_key())
    C = elgamal.encrypt(M, k)
    print('Encrypted:', C)
    print('Decrypted:', elgamal.decrypt(C))

def dsa():
    # Given values
    p = 59
    q = 29
    g = 10
    xA = 2
    k = 3
    H_M = 19  # Assuming a hash value for the message M

    # Create an instance of DSA
    dsa = DSA(p, q, g, xA)

    # Calculate the public key
    yA = dsa.get_public_key()

    # Sign the message hash
    signature = dsa.sign(H_M, k)

    # Verify the signature
    is_valid = dsa.verify(H_M, signature)

    # Print the results
    print(f"Public key (yA): {yA}")
    print(f"Signature (r, s): {signature}")
    print(f"Is the signature valid? {is_valid}")

if __name__ == '__main__':
    # rsa()
    # diffie_hellman()
    # elgamal()
    dsa()