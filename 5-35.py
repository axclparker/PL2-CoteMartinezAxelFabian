import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

x, y, c = sp.symbols('x y c')

f_xy = c * x * y

integral_c = sp.integrate(sp.integrate(f_xy, (x, 0, 3)), (y, 0, 3))
c_value = sp.solve(integral_c - 1, c)[0]  
print(f"Constante de normalización c = {c_value}")

f_xy = f_xy.subs(c, c_value)

# a. P(X < 2.5, Y < 3)
p_a = sp.integrate(sp.integrate(f_xy, (y, 0, 3)), (x, 0, 2.5))
print(f"P(X < 2.5, Y < 3) = {p_a}")

# b. P(X < 2.5)
p_b = sp.integrate(sp.integrate(f_xy, (y, 0, 3)), (x, 0, 2.5))
print(f"P(X < 2.5) = {p_b}")

# c. P(1 < Y < 2.5)
p_c = sp.integrate(sp.integrate(f_xy, (y, 1, 2.5)), (x, 0, 3))
print(f"P(1 < Y < 2.5) = {p_c}")

# d. P(X > 1.8, 1 < Y <= 2.5)
p_d = sp.integrate(sp.integrate(f_xy, (y, 1, 2.5)), (x, 1.8, 3))
print(f"P(X > 1.8, 1 < Y <= 2.5) = {p_d}")

# e. E(X)
e_x = sp.integrate(sp.integrate(x * f_xy, (y, 0, 3)), (x, 0, 3))
print(f"E(X) = {e_x}")

# f. E(Y)
e_y = sp.integrate(sp.integrate(y * f_xy, (y, 0, 3)), (x, 0, 3))
print(f"E(Y) = {e_y}")
