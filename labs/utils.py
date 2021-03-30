import math
import random
import numpy as np


def gcd(a, b):
    return int(gcd_core(math.fabs(a), math.fabs(b)))


def gcd_core(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def gcd_extended(a, b):
    if a == 0:
        return b, 0, 1

    gcd_result, x1, y1 = gcd_extended(b % a, a)

    x = y1 - (b // a) * x1
    y = x1

    return gcd_result, x, y


def euler(n):
    result = n

    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n = n // p
            result *= 1.0 - (1.0 / float(p))
        p = p + 1

    if n < 1:
        result *= 1.0 - (1.0 / float(n))

    return int(result)


def primes(start, end):
    res = []

    for num in range(start, end):
        status = True

        for divisor in range(2, math.isqrt(num)):
            if num % divisor == 0:
                status = False
                break
        if status:
            res.append(num)
    return res


def generate_primes(start=2, end=2):
    primes_nums = primes(start, end)
    return primes_nums[random.randint(0, len(primes_nums) - 1)]


def is_prime(n):
    if n % 2 == 0:
        return n == 2

    d = 3
    while d * d <= n and n % d != 0:
        d += 2

    return d * d > n


def is_perfect_square(x):
    return x == math.isqrt(x) ** 2


# ab + by = c
def solve_diophantine_equation(a, b, c):
    should_solve = c % gcd(a, b) == 0
    if should_solve:
        _, xg, yg = gcd_extended(a, b)

        return xg * c, yg * c

    return math.nan, math.nan


# ax = b % m
def solve_comparison_equation(a, b, m):
    d = gcd(a, m)

    if b % d == 0:
        x, _ = solve_diophantine_equation(a, m, b)
        return x % m

    return math.nan


def solve_comparison_fermat_equation(a, b, m):
    d = gcd(a, m)

    if d == 1:
        x = str(((a ** (euler(m) - 1)) * b) % m)
    else:
        if b % d == 0:
            a1 = a // d
            b1 = b // d
            m1 = m // d

            x1 = ((a1 ** (euler(m1) - 1)) * b1) % m1
            x = str(m1) + "k + " + str(x1) + "(mod " + str(m) + "), k ∈ {0,...," + str(d - 1) + "}"
        else:
            x = "no solutions"

    return x


def get_relative_primes(p, start=1, end=1):
    res = []

    if end == 0:
        end = p

    for i in range(start, end):
        if gcd(i, p) == 1:
            res.append(i)

    return res


def generate_relative_primes(n):
    relative_with_num = get_relative_primes(n, 2, 0)
    return relative_with_num[random.randint(0, len(relative_with_num) - 1)]


def get_primitive_roots(m):
    for r in range(2, m):
        for p in range(1, m):
            value = (r ** p) % m

            if value == 1:
                if p == m - 1:
                    prime_numbers = get_relative_primes(m - 1, 1, m - 1)
                    res = []

                    for rp in prime_numbers:
                        res.append(int((r ** rp) % m))

                    return res
                else:
                    break
    return []


def generate_primitive_root(n):
    roots = get_primitive_roots(n)
    return roots[random.randint(0, len(roots) - 1)]


def chinese_remainder(b, m):
    n = len(b)

    for i in range(n):
        for j in range(n):
            if i != j:
                if gcd(m[i], m[j]) != 1:
                    return math.nan

    module = np.prod(m)
    ms = []
    m_inv = []

    for i in range(n):
        mod = 1

        for j in range(n):
            if i != j:
                mod *= m[j]
        m_ = solve_comparison_equation(mod, 1, m[i])

        ms.append(mod)
        m_inv.append(m_)

    x = 0
    for i in range(n):
        x += ms[i] * m_inv[i] * b[i]
    x %= module

    # print()
    # print(f"M = {mod}")
    # print(f"Ms = {ms}")
    # print(f"M inversions = {m_inv}")
    # print(f"x = {x}")
    # print()

    return x
