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
    def extend_euclid(a, mod):
        def sub_ex_euclid(num, _mod):
            if _mod == 0:
                return [num, 1, 0]
            else:
                d, x, y = sub_ex_euclid(_mod, num % _mod)
                return d, y, x - num // _mod * y

        return sub_ex_euclid(a, mod)[1]

    @staticmethod
    def pow(a, m, mod):
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
