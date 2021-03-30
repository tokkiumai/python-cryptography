import utils


print(f"(GCD), (256, 384): {utils.gcd(256, 384)}")
print(f"(GCD), (714, 218): {utils.gcd(714, 218)}")
print(f"(GCD), (516, 438): {utils.gcd(516, 438)}")
print(f"(GCD), (735, 525): {utils.gcd(735, 525)}")

print()

print(f"(Euler), n = 63: {utils.euler(63)}")
print(f"(Euler), n = 100: {utils.euler(100)}")
print(f"(Euler), n = 525: {utils.euler(525)}")
print(f"(Euler), n = 31: {utils.euler(31)}")
print(f"(Euler), n = 274: {utils.euler(274)}")

print()

print(f"(Primitive roots), n = 7: {utils.get_primitive_roots(7)}")
print(f"(Primitive roots), n = 11: {utils.get_primitive_roots(11)}")
print(f"(Primitive roots), n = 13: {utils.get_primitive_roots(13)}")
print(f"(Primitive roots), n = 19: {utils.get_primitive_roots(19)}")
print(f"(Primitive roots), n = 23: {utils.get_primitive_roots(23)}")

print()

print(f"(Diophantine), 5x + 7y = 14: {utils.solve_diophantine_equation(5, 7, 14)}")
print(f"(Diophantine), 27x + 36y = 32: {utils.solve_diophantine_equation(27, 36, 32)}")
print(f"(Diophantine), 10x + 12y = 13: {utils.solve_diophantine_equation(10, 12, 13)}")
print(f"(Diophantine), 54x + 48y = 128: {utils.solve_diophantine_equation(54, 48, 128)}")
print(f"(Diophantine), 14x + 27y = 49: {utils.solve_diophantine_equation(14, 27, 49)}")
print(f"(Diophantine), 150x + 75y = 216: {utils.solve_diophantine_equation(150, 75, 216)}")
print(f"(Diophantine), 18x + 35y = 36: {utils.solve_diophantine_equation(18, 35, 36)}")
print(f"(Diophantine), 50x + 44y = 121: {utils.solve_diophantine_equation(50, 44, 121)}")

print()

print(f"(Comparison), 3x = 19 mod 34: {utils.solve_comparison_equation(3, 19, 34)}")
print(f"(Comparison), 15x = 35 mod 100: {utils.solve_comparison_equation(15, 35, 100)}")
print(f"(Comparison), 16x = 19 mod 34: {utils.solve_comparison_equation(16, 19, 34)}")
print(f"(Comparison), 4x = 3 mod 7: {utils.solve_comparison_equation(4, 3, 7)}")
print(f"(Comparison), 7x = 11 mod 39: {utils.solve_comparison_equation(7, 11, 39)}")
print(f"(Comparison), 9x = 21 mod 48: {utils.solve_comparison_equation(9, 21, 48)}")
print(f"(Comparison), 22x = 11 mod 38: {utils.solve_comparison_equation(22, 11, 38)}")
print(f"(Comparison), 11x=  5 mod 17: {utils.solve_comparison_equation(11, 5, 17)}")
print(f"(Comparison), 5x = 8 mod 21: {utils.solve_comparison_equation(5, 8, 21)}")
print(f"(Comparison), 14x = 8 mod 50: {utils.solve_comparison_equation(14, 8, 50)}")
print(f"(Comparison), 6x = 7 mod 22: {utils.solve_comparison_equation(6, 7, 22)}")
print(f"(Comparison), 2x = 5 mod 11: {utils.solve_comparison_equation(2, 5, 1)}")
