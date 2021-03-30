import polynomial


print(f"101    * 11  = {polynomial.gf2_multiply('101',    '11')}")
print(f"1011   * 11  = {polynomial.gf2_multiply('1011',   '11')}")
print(f"1101   * 101 = {polynomial.gf2_multiply('1101',   '101')}")
print(f"10101  * 111 = {polynomial.gf2_multiply('10101',  '111')}")
print(f"10111  * 11  = {polynomial.gf2_multiply('10111',  '11')}")
print(f"101101 * 111 = {polynomial.gf2_multiply('101101', '111')}")

print()

print(f"101    / 11  = {polynomial.gf2_division('101',    '11')}")
print(f"1011   / 11  = {polynomial.gf2_division('1011',   '11')}")
print(f"1101   / 101 = {polynomial.gf2_division('1101',   '101')}")
print(f"10101  / 111 = {polynomial.gf2_division('10101',  '111')}")
print(f"10111  / 11  = {polynomial.gf2_division('10111',  '11')}")
print(f"101101 / 111 = {polynomial.gf2_division('101101', '111')}")

print()

print(f"GCD(100001, 1111)   = {polynomial.gf2_gcd('100001', '1111')}")
print(f"GCD(110001, 11011)  = {polynomial.gf2_gcd('110001', '11011')}")
print(f"GCD(10001,  101101) = {polynomial.gf2_gcd('10001',  '101101')}")
print(f"GCD(111010, 101110) = {polynomial.gf2_gcd('111010', '101110')}")
