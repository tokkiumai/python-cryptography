import math


def gf2_core(a, b):
    if a == b:
        return "1", "0"

    deg_a = len(a)-1
    deg_b = len(b)-1

    if deg_a < deg_b:
        return "0", a

    if deg_a == deg_b:
        return "1", gf2_add(a, b)

    deg_m = deg_a - deg_b

    m = ["0" for i in range(0, deg_m+1)]

    m[0] = "1"
    m = "".join(m)

    mul = gf2_multiply(b, m)
    r = gf2_add(a, mul)

    return m, r


def gf2_add(a, b):
    res_len = max(len(a), len(b))

    op_a = "".join(["0" for _ in range(0, res_len - len(a))])
    op_b = "".join(["0" for _ in range(0, res_len - len(b))])
    op_a += a
    op_b += b

    res = ""
    for j in range(0, res_len):
        if op_a[j] == "1" and op_b[j] == "0" or op_a[j] == "0" and op_b[j] == "1":
            res += "1"
        else:
            res += "0"

    return str(int(res))


def gf2_multiply(a, b):
    layer_len = len(a) + len(b) - 1
    layers = []

    for i in range(len(b) - 1, -1, -1):
        if b[i] == "1":
            layer = [0 for s in range(0, layer_len)]
            for j in range(len(a) - 1, -1, -1):
                layer[i + j] = int(a[j])
            layers.append(layer)

    res = ""
    for j in range(0, layer_len):
        units_quantity = 0
        for i in range(0, len(layers)):
            if layers[i][j] == 1:
                units_quantity += 1
        if units_quantity % 2 != 0:
            res += "1"
        else:
            res += "0"

    return res


def gf2_division(a, b):
    multiplier_bites = []
    rest = ""

    r = a

    while True:
        m, r = gf2_core(r, b)
        multiplier_bites.append(m)

        if m == "1" or m == "0":
            rest = r
            break
        if r == "0":
            break

    multiplier = multiplier_bites[0]
    if len(multiplier_bites) > 1:
        for i in range(1, len(multiplier_bites)):
            multiplier = gf2_add(multiplier, multiplier_bites[i])

    return multiplier, rest


def gf2_gcd(a, b):
    a1 = a
    b1 = b

    result = math.nan

    while True:
        _, r = gf2_core(a1, b1)

        if r == "0":
            break

        result = r

        a1 = b1
        b1 = r

    return result


def is_reducible(p):
    d = int("0b" + p, 2)

    for i in range(2, d):
        if gf2_division(p, bin(i)[2:])[1] == "0":
            return False

    return True


def is_primitive(polynomial):
    power = len(polynomial) - 1
    m = 2 ** power - 1

    lst = generate_polynomial(power, m)
    if gf2_division(lst[len(lst) - 1], polynomial)[1] == "0":
        for i in range(0, len(lst) - 1):
            d, m = gf2_division(lst[i], polynomial)
            print(lst[i] + "  " + polynomial + "  " + d + "  " + m)
            if m == "0":
                return False
        return True

    return False


def generate_polynomial(n, m):
    lst = list()

    for p in range(n, m):
        new_pol = "1" + ''.join(["0" for i in range(p)]) + "1"
        lst.append(new_pol)

    return lst


def get_primitive_roots(polynomial, field):
    d = int("0b" + polynomial, 2)

    first_root = None
    mod_list = None

    for i in range(2, d):
        x = i
        mod_list = [bin(x)[2:]]

        for j in range(2, field):
            x *= i
            mod = gf2_division(bin(x)[2:], polynomial)[1]
            mod_list.append(mod)

            if mod == "1":
                if j != field - 1:
                    break
                else:
                    first_root = i

        if first_root:
            break

    result = list()
    for j in range(0, field - 1):
        if gf2_gcd(j + 1, field - 1) == 1:
            result.append(mod_list[j])

    return result
