import random


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


def main():
    with open('test_table.txt', 'w') as File:
        header = "Число     | "
        for test_num in range(1, 101):
            if test_num < 10:
                header += f"{test_num} тест  | "
            else:
                header += f"{test_num} тест | "
        File.write(f"{header}\n")

        for number in range(2, 10000):
            row = ""
            if number < 10:
                row += f"{number}         | "
            elif number < 100:
                row += f"{number}        | "
            elif number < 1000:
                row += f"{number}       | "
            elif number < 10000:
                row += f"{number}      | "
            elif number < 100000:
                row += f"{number}     | "
            elif number < 1000000:
                row += f"{number}    | "
            elif number < 1000000:
                row += f"{number}   | "
            elif number < 1000000:
                row += f"{number}  | "
            else:
                row += f"{number}"

            for iter_count in range(1, 101):
                res = miller_rabin_test(number, iter_count)
                if res:
                    row += "   +    | "
                else:
                    row += "   -    | "

            File.write(f"{row}\n")
