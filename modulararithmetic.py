import math
from collections import defaultdict


class Module:
    @staticmethod
    def isprime(a):
        i = 2
        while i * i <= a:
            if a % i == 0:
                return False
            i += 1
        return True

    @staticmethod
    def extended_euclid(a, mod):
        if math.gcd(a, mod) != 1:
            raise ValueError("error")

        def sub_ex_euclid(num, _mod):
            if _mod == 0:
                return [num, 1, 0]
            else:
                d, x, y = sub_ex_euclid(_mod, num % _mod)
                return d, y, x - num // _mod * y

        res = sub_ex_euclid(a, mod)[1]
        return res if res > 0 else res + mod

    @staticmethod
    def pow_2(a, m, mod):
        a = a % mod
        num = bin(m)
        res = 1
        val = a
        for i, v in enumerate(num[::-1]):
            if i > 0:
                val = (val * val) % mod
            if v == '1':
                res = (res * val) % mod
            elif v == 'b':
                break
        return res

    @staticmethod
    def euler_function(p):
        if Module.isprime(p):
            return p - 1
        d = Module.analysis_prime(p)
        res = 1
        for k, v in d.items():
            res *= math.pow(k, v) - math.pow(k, v - 1)
        return int(res)

    @staticmethod
    def analysis_prime(x):
        if x < 2:
            return x
        d = defaultdict(int)
        if Module.isprime(x):
            d[x] = 1
            return d
        num = 2
        _pow = 0
        while x != 1 or num < x:
            if x % num == 0:
                x //= num
                _pow += 1
                d[num] = _pow
            else:
                _pow = 0
                num += 1
        return d

    @staticmethod
    def pow_euler(a, m, mod):
        eu_n = Module.euler_function(mod)
        ex = m % eu_n
        res = a % mod
        res = res ** ex
        res %= mod
        return res

    @staticmethod
    def pow_chinese(A, exp, mod):
        mul = 1
        m = []
        for i, v in Module.analysis_prime(mod).items():
            mul *= i * v
            m.append(i * v)
        res = 0
        for i in range(len(m)):
            M = mul // m[i]
            _M = Module.extended_euclid(M, m[i])
            c = M * (_M % m[i])
            a = pow(A, exp, m[i])
            res = (res + (a * c) % mod) % mod

        return res

    @staticmethod
    def solve_equation_chinese(a: list, m: list):
        if len(a) != len(m):
            raise ValueError("The length of a and m should be the same")

        res = 0
        mul = 1
        for i in m:
            mul *= i

        for i in range(len(a)):
            M = mul // m[i]
            _M = Module.extended_euclid(M, m[i])
            c = M * (_M % m[i])
            res += a[i] * c
        return res % mul

    @staticmethod
    def is_primitive_root(a, n):
        e = Module.euler_function(n)
        for i in range(1, e):
            if a ** i % n == 1:
                return False
        return True

    @staticmethod
    def logarit(a, b, p):
        i = 0
        while True:
            if a ** i % p == b:
                return i
            i += 1


if __name__ == '__main__':
    print('Bai 1:', Module.pow_2(239, 6653, 6653))
    print('Bai 2:', Module.extended_euclid(1974, 7841))
    print('Bai 3:', Module.pow_2(311, 821, 6311))
    print('Bai 4:', Module.euler_function(3312))
    print('Bai 5:', Module.pow_euler(38, 2934, 220))
    print('Bai 6:', Module.pow_chinese(241, 59, 63307))
    print('Bai 7:', Module.solve_equation_chinese([5, 5, 6], [19, 11, 13]))
    print('Bai 8:', Module.is_primitive_root(5, 263))
    print('Bai 9:', Module.logarit(2, 7, 11))
