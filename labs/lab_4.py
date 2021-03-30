import prime_test
import factorization


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

print()

print(f"(Origin), n = 483: {factorization.original(483)}")
print(f"(Origin), n = 1207: {factorization.original(1207)}")
print(f"(Origin), n = 561: {factorization.original(561)}")
print(f"(Origin), n = 1219: {factorization.original(1219)}")

print(f"(P-1), n = 483: {factorization.pollard_p_minus_one(483)}")
print(f"(P-1), n = 1207: {factorization.pollard_p_minus_one(1207)}")
print(f"(P-1), n = 561: {factorization.pollard_p_minus_one(561)}")
print(f"(P-1), n = 1219: {factorization.pollard_p_minus_one(1219, b=17, m=28, a=2)}")

print()
print(f"(PO), n = 483: {factorization.pollard_po(483)}")
print(f"(PO), n = 1207: {factorization.pollard_po(1207)}")
print(f"(PO), n = 561: {factorization.pollard_po(561)}")
print(f"(PO), n = 1219: {factorization.pollard_po(1219)}")

print()
print(f"(Fermat), n = 483: {factorization.fermat(483)}")
print(f"(Fermat), n = 1207: {factorization.fermat(1207)}")
print(f"(Fermat), n = 561: {factorization.fermat(561)}")
print(f"(Fermat), n = 1219: {factorization.fermat(1219)}")
