import random


def original_test(n):
    for i in range(2, round(n / 2)):
        if n % i == 0:
            return False

    return True


def fermat_test(n, iterations=1000):
    for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]:
        if n % p == 0:
            return n == p

    for _ in range(iterations):
        x = random.randint(1, n - 1)

        if x ** (n - 1) % n != 1:
            return False

    return True


def square_root_test(n, iterations=1000):
    for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]:
        if n % p == 0:
            return n == p

    for _ in range(iterations):
        x = random.randint(2, round(n / 2))

        if x * x % n == 1:
            return False

    return True


def miller_rabin_test(n, iterations=1000):
    if n < 2:
        return False

    for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]:
        if n % p == 0:
            return n == p

    s, q = 0, n - 1
    while q % 2 == 0:
        s, q = s + 1, q / 2

    for _ in range(iterations):
        a = random.randint(2, n - 1)
        x = pow(a, int(q), int(n))

        if x == 1 or x == n - 1:
            continue

        for _ in range(1, s):
            x = x * x % n
            if x == 1:
                return False
            if x == n - 1:
                break

    return True
