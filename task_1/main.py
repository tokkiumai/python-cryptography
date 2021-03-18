from typing import Tuple


def extended_euclid(a: int, b: int) -> Tuple[int, int]:
    """
    >>> extended_euclid(10, 6)
    (-1, 2)
    >>> extended_euclid(7, 5)
    (-2, 3)
    """
    if b == 0:
        return 1, 0

    (x, y) = extended_euclid(b, a % b)
    k = a // b

    return y, x - k * y


def chinese_remainder(n1: int, r1: int, n2: int, r2: int) -> int:
    """
    >>> chinese_remainder(5,1,7,3)
    31
    >>> chinese_remainder(6,1,4,3)
    14
    """
    (x, y) = extended_euclid(n1, n2)

    m = n1 * n2
    n = r2 * x * n1 + r1 * y * n2

    return (n % m + m) % m


if __name__ == '__main__':
    from doctest import testmod

    testmod(name="extended_euclid", verbose=True)
    testmod(name="chinese_remainder", verbose=True)
