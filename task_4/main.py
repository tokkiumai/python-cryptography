# Реализовать программный продукт обратного преобразования DES для введенных двоичных последовательностей шифртекста и ключа.
# Для реализации криптоалгоритмов запрещено пользоваться встроенными библиотеками используемых языков.

# -- Permutation tables and constants -------------------------------------

MODE = {
    'ECB': 'ECB',  # Electric Codebook
    'CBC': 'CBC',  # Cipher Block Chaining
    'CFB': 'CFB',  # Cipher Feedback
}

# Subkeys generation tables
PC_1 = [
    57, 49, 41, 33, 25, 17, 9,
    1, 58, 50, 42, 34, 26, 18,
    10, 2, 59, 51, 43, 35, 27,
    19, 11, 3, 60, 52, 44, 36,
    63, 55, 47, 39, 31, 23, 15,
    7, 62, 54, 46, 38, 30, 22,
    14, 6, 61, 53, 45, 37, 29,
    21, 13, 5, 28, 20, 12, 4,
]

PC_2 = [
    14, 17, 11, 24, 1, 5,
    3, 28, 15, 6, 21, 10,
    23, 19, 12, 4, 26, 8,
    16, 7, 27, 20, 13, 2,
    41, 52, 31, 37, 47, 55,
    30, 40, 51, 45, 33, 48,
    44, 49, 39, 56, 34, 53,
    46, 42, 50, 36, 29, 32,
]

# Initial message permutation table
IP = [
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9, 1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7,
]

# Subkeys shifting schedule
Shift_Schedule = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

# Expand table from 32 to 48 bits
E = [
    32, 1, 2, 3, 4, 5,
    4, 5, 6, 7, 8, 9,
    8, 9, 10, 11, 12, 13,
    12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21,
    20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29,
    28, 29, 30, 31, 32, 1,
]

# S-Boxes
S = [
    [
        [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],
    ],
    [
        [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
        [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
        [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
        [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],
    ],
    [
        [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
        [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
        [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
        [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],
    ],
    [
        [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
        [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
        [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
        [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],
    ],
    [
        [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
        [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
        [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
        [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],
    ],
    [
        [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
        [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
        [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
        [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],
    ],
    [
        [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
        [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
        [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
        [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],
    ],
    [
        [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
        [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
        [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
        [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],
    ],
]

# Feistel function permutation
P = [
    16, 7, 20, 21,
    29, 12, 28, 17,
    1, 15, 23, 26,
    5, 18, 31, 10,
    2, 8, 24, 14,
    32, 27, 3, 9,
    19, 13, 30, 6,
    22, 11, 4, 25,
]

# Final permutation table
IP_INV = [
    40, 8, 48, 16, 56, 24, 64, 32,
    39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30,
    37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28,
    35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26,
    33, 1, 41, 9, 49, 17, 57, 25,
]


# -- Helpers -------------------------------------

def apply_permutation_table(table, lst):
    permutated = []
    for i in table:
        permutated.append(lst[i - 1])
    return permutated


def preprocess_message(mes):
    diff = 16 - len(mes)

    binary_string = []
    for letter in mes:
        for b in alphabet[letter]:
            binary_string.append(b)

    for i in range(diff):
        for b in [0, 0, 0, 0]:
            binary_string.append(b)

    return binary_string


def print_bytes(lst, mes=''):
    byte_string = "".join(list(map(lambda x: str(x), lst)))
    print(f"{mes}: {byte_string}")


def shift_left(lst):
    left_el = lst[0]
    new_list = lst[1:]
    new_list.append(left_el)
    return new_list


def bytelist_to_string(lst):
    return "".join(list(map(lambda x: str(x), lst)))


def bytelist_to_decimal(lst):
    bin_str = bytelist_to_string(lst)
    return int(bin_str, 2)


def bytelist_to_hexdecimal(lst):
    bin_str = bytelist_to_string(lst)
    return hex(int(bin_str, 2))


def decimal_to_bytelist(num):
    binary = bin(num)[2:]
    diff = 4 - len(binary)

    res = []
    for i in range(diff):
        res.append(0)
    for b in binary:
        res.append(int(b))

    return res


def hex_to_bytelist(val):
    binary = bin(int(val[:64], 16))[2:]
    diff = 64 - len(binary)
    res = [0 for _ in range(diff)]
    for b in binary:
        res.append(b)
    return res


def text_to_binary_blocks(text):
    bytelist = []
    for letter in text:
        binary = bin(ord(letter))[2:]
        for b in binary:
            bytelist.append(int(b))

    while len(bytelist) % 64 != 0:
        bytelist.append(0)

    blocks = []
    step = 64
    for i in range(0, len(bytelist), step):
        block = bytelist[i:i + step]
        blocks.append(block)

    return blocks


# -- Core -------------------------------------

def create_subkeys(hex_key):
    key = hex_to_bytelist(hex_key)

    print("------------SUBKEYS GENERATION------------\n")
    print("Length of the original K:", len(key))
    print_bytes(key, 'Original key')

    # PC_1 permutation
    key_plus = apply_permutation_table(PC_1, key)
    print("\nLength of the permutated by PC_1 key:", len(key_plus))
    print_bytes(key_plus, 'Permutated by PC_1 key')

    C = key_plus[:28]
    D = key_plus[28:]

    # INFO
    print("Length of the C:", len(C))
    print_bytes(C, "\nC")
    print("Length of the D:", len(D))
    print_bytes(D, "D")

    subkeys = []

    # Shifting keys and generating subkeys
    C_sub_current = C.copy()
    D_sub_current = D.copy()

    print("\nSHIFTS:")
    i = 0
    for shift_count in Shift_Schedule:
        for c in range(shift_count):
            C_sub_current = shift_left(C_sub_current)
            D_sub_current = shift_left(D_sub_current)
            print_bytes(C_sub_current, f"C{i}")
            print_bytes(D_sub_current, f"D{i}")

        i += 1
        subkey = C_sub_current + D_sub_current
        subkey = apply_permutation_table(PC_2, subkey)
        subkeys.append(subkey)

    # INFO
    print("\nSUBKEYS:")
    for i in range(len(subkeys)):
        print_bytes(subkeys[i], f"K{i}")
    print()

    return subkeys


def xor_blocks(block1, block2):
    result = []
    for i in range(len(block1)):
        # print("XOR:", int(block1[i]), int(block2[i]), int(block1[i]) == int(block2[i]))
        if int(block1[i]) == int(block2[i]):
            result.append(0)
        else:
            result.append(1)
    return result


def SBox(index, block):
    i_lst = block[:1] + block[5:]
    j_lst = block[1:5]

    i = bytelist_to_decimal(i_lst)
    j = bytelist_to_decimal(j_lst)

    sbox_res = S[index][i][j]
    sbox_res = decimal_to_bytelist(sbox_res)

    return sbox_res


def feistel_func(block, subkey):
    expanded = apply_permutation_table(E, block)
    xored = xor_blocks(expanded, subkey)

    S_res = []
    start = 0
    end = 6

    for i in range(8):
        val = SBox(i, xored[start:end])
        for v in val:
            S_res.append(v)
        start += 6
        end += 6

    S_Permutated = apply_permutation_table(P, S_res)

    return S_Permutated


def encryption_rounds(R0, L0, subkeys, log):
    if log:
        print("\nEncryption rounds:")

    R = R0.copy()
    L = L0.copy()
    Ln = []
    Rn = []
    for i in range(0, 16):
        Ln = R.copy()
        Rn = xor_blocks(L, feistel_func(R, subkeys[i]))
        L = Ln.copy()
        R = Rn.copy()

        if log:
            print_bytes(Ln, f"L{i}")
            print_bytes(Rn, f"R{i}")

    return Rn + Ln


def encrypt_block(M, subkeys, log):
    permutated_M = apply_permutation_table(IP, M)

    L = permutated_M[:32]  # Left perm message part
    R = permutated_M[32:]  # Right perm message part

    Cipher = encryption_rounds(R, L, subkeys, log=log)
    PCipher = apply_permutation_table(IP_INV, Cipher)

    cipher_hex = bytelist_to_hexdecimal(PCipher)[2:]

    if log:
        print("\nPreprocessed message length:", len(M))
        print_bytes(M, "Preprocessed message")
        print("\nPermutated M by IP length:", len(permutated_M))
        print_bytes(permutated_M, "Permutated M by IP:")
        print_bytes(L, "\nL")
        print_bytes(R, "R")
        print()
        print_bytes(Cipher, '\nCipher')
        print_bytes(PCipher, "Permutated cipher")

    return cipher_hex, PCipher


def decrypt_block(block, subkeys, log):
    # Apply inverse to IP_INV (IP) table
    cipher = apply_permutation_table(IP, block)
    # Start decryption
    Rn, Ln = cipher[:32], cipher[32:]

    permutated_M = decryption_rounds(Rn, Ln, subkeys, log=log)
    M = apply_permutation_table(IP_INV, permutated_M)

    if log:
        print("\nBlock lenght", len(block))
        print_bytes(block, 'Block')
        print_bytes(cipher, "Cipher")
        print()
        print_bytes(Ln, "Ln")
        print_bytes(Rn, "Rn")
        print_bytes(permutated_M, f"\nPermutated binary message")
        print_bytes(M, "Decrypted binary message")

    return M


def decryption_rounds(R0, L0, subkeys, log):
    if log:
        print("\nDecryption rounds:")

    Ln = L0.copy()
    Rn = R0.copy()
    L = []
    R = []
    for i in reversed(range(0, 16)):
        R = Ln.copy()
        L = xor_blocks(Rn, feistel_func(Ln, subkeys[i]))
        Ln = L.copy()
        Rn = R.copy()

        if log:
            print_bytes(L, f"L{i}")
            print_bytes(R, f"R{i}")

    return L + R


# -- Wrappers
def DES_encrypt(mes, subkeys, mode='ECB', C0=None):
    print("------------FIRST BLOCK ENCRYPTION------------\n")
    print('Mode:', mode)

    common_cipher = []
    binary_text_blocks = text_to_binary_blocks(mes)
    log = True  # For logging only one block
    m_prev = None
    if mode == MODE['CBC'] or mode == MODE['CFB']:
        m_prev = hex_to_bytelist(C0)

    for M in binary_text_blocks:
        if mode == MODE['ECB']:
            cipher_hex, _ = encrypt_block(M, subkeys, log=log)
            common_cipher.append(cipher_hex)

        elif mode == MODE['CBC']:
            block = xor_blocks(M, m_prev)
            cipher_hex, cipher_bin = encrypt_block(block, subkeys, log=log)
            m_prev = cipher_bin
            common_cipher.append(cipher_hex)

        elif mode == MODE['CFB']:
            _, D = encrypt_block(m_prev, subkeys, log=log)
            print_bytes(D, 'D')
            cipher_bin = xor_blocks(M, D)
            cipher_hex = bytelist_to_hexdecimal(cipher_bin)[2:]
            common_cipher.append(cipher_hex)
            m_prev = cipher_bin

        log = False

    joined_cipher = "".join(common_cipher)  # Join ['hex', 'hex', ...] to one string
    print(f"\nEncrypted message (hex): {joined_cipher}")

    return joined_cipher


def DES_decrypt(enc, subkeys, mode='ECB', C0=None):
    print("\n------------FIRST BLOCK DECRYPTION------------\n")
    print(f"Encrypted message length:", len(enc), end='\n\n')

    hex_list = []
    print("Encrypted blocks:")
    step = 16
    for i in range(0, len(enc), step):
        hex_list.append(enc[i:i + step])
        print(enc[i:i + step], len(enc[i:i + step]))

    deciphered_binary_blocks = []
    m_prev = hex_to_bytelist(C0)
    log = True

    for hex_block in hex_list:
        if mode == MODE['ECB']:
            block = hex_to_bytelist(hex_block)
            M = decrypt_block(block, subkeys, log=log)
            deciphered_binary_blocks.append(M)

        elif mode == MODE['CBC']:
            block = hex_to_bytelist(hex_block)
            D = decrypt_block(block, subkeys, log=log)
            M = xor_blocks(D, m_prev)
            deciphered_binary_blocks.append(M)
            m_prev = block.copy()

        elif mode == MODE['CFB']:
            _, D = encrypt_block(m_prev, subkeys, log=log)
            block = hex_to_bytelist(hex_block)
            M = xor_blocks(block, D)
            deciphered_binary_blocks.append(M)
            m_prev = block

        log = False

    deciphered = "".join(list(map(lambda x: bytelist_to_string(x), deciphered_binary_blocks)))
    binary_letters = [deciphered[i:i + 11] for i in range(0, len(deciphered), 11)]
    letters = list(map(lambda x: chr(int(x, 2)), binary_letters))

    result = "".join(letters)
    print("\nDecrypted message: ", result)

    return result


# -------------------- Usage ----------------------

key = "0E329232EA6D0D73"
message = "somemessage"
C0 = '0E329232EA6D0D73'
mode = MODE['CFB']

subkeys = create_subkeys(key)
encrypted = DES_encrypt(message, subkeys, mode=mode, C0=C0)
decrypted = DES_decrypt(encrypted, subkeys, mode=mode, C0=C0)

# print('Task 1:')
# S_indexes = [2, 3, 6, 1]
# addresses = [[1, 1, 0, 1, 1, 1], [0, 0, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1]]
# for i in range(len(S_indexes)):
#     S_bin = SBox(S_indexes[i], addresses[i])
#     S_dec = bytelist_to_decimal(S_bin)
#     print("Sbox", i+1, ":", bytelist_to_string(S_bin), S_dec)

# print('\nTask 2:')
# for i in range(8):
#     S_bin = SBox(i, [0, 0, 0, 0, 0, 0])
#     S_dec = bytelist_to_decimal(S_bin)
#     print("Sbox", i+1, ":", bytelist_to_string(S_bin), S_dec)

# print('\nTask 3:')
# for i in range(8):
#     S_bin = SBox(i, [1, 1, 1, 1, 1, 1])
#     S_dec = bytelist_to_decimal(S_bin)
#     print("Sbox", i+1, ":", bytelist_to_string(S_bin), S_dec)