import prime_test


print(f"(Square root), n = 23: {prime_test.square_root_test(23)}")
print(f"(Square root), n = 41: {prime_test.square_root_test(41)}")
print(f"(Square root), n = 15: {prime_test.square_root_test(15)}")
print(f"(Square root), n = 35: {prime_test.square_root_test(35)}")
print(f"(Square root), n = 561: {prime_test.square_root_test(561)}")

print()

print(f"(Fermat), n = 23: {prime_test.fermat_test(23)}")
print(f"(Fermat), n = 41: {prime_test.fermat_test(41)}")
print(f"(Fermat), n = 15: {prime_test.fermat_test(15)}")
print(f"(Fermat), n = 35: {prime_test.fermat_test(35)}")
print(f"(Fermat), n = 561: {prime_test.fermat_test(561)}")

print()

print(f"(Miller-Rabin), n = 23: {prime_test.miller_rabin_test(23)}")
print(f"(Miller-Rabin), n = 41: {prime_test.miller_rabin_test(41)}")
print(f"(Miller-Rabin), n = 15: {prime_test.miller_rabin_test(15)}")
print(f"(Miller-Rabin), n = 35: {prime_test.miller_rabin_test(35)}")
print(f"(Miller-Rabin), n = 561: {prime_test.miller_rabin_test(561)}")
