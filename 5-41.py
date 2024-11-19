import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

x, y, c = sp.symbols('x y c')

region_conditions = (x > 0, x < 4, y > 0, y < 4, y > x - 1, y < x + 1)

f_xy = c

joint_integral = sp.integrate(f_xy, (y, x - 1, x + 1), (x, 0, 4))
c_value = sp.solve(joint_integral - 1, c)[0]

f_xy = c_value

# a. P(X < 0.5, Y < 0.5)
prob_x_y = sp.integrate(f_xy, (y, 0, 0.5), (x, 0, 0.5))

# b. P(X < 0.5)
prob_x = sp.integrate(f_xy, (y, x - 1, x + 1), (x, 0, 0.5))

# c. E(X) y E(Y)
E_x = sp.integrate(x * f_xy, (y, x - 1, x + 1), (x, 0, 4))
E_y = sp.integrate(y * f_xy, (y, x - 1, x + 1), (x, 0, 4))

# d. Distribución condicional de X dado Y = 1
f_x_given_y1 = f_xy.subs(y, 1)
f_y1 = sp.integrate(f_xy.subs(y, 1), (x, 0, 4))

conditional_distribution = f_x_given_y1 / f_y1
conditional_distribution_simplified = sp.simplify(conditional_distribution)

print(f"Valor de c: {c_value}")
print(f"P(X < 0.5, Y < 0.5): {prob_x_y}")
print(f"P(X < 0.5): {prob_x}")
print(f"E(X): {E_x}")
print(f"E(Y): {E_y}")
print(f"Distribución condicional de X dado Y = 1: {conditional_distribution_simplified}")

x_vals = np.linspace(0, 4, 400)
y_vals = np.linspace(0, 4, 400)
X, Y = np.meshgrid(x_vals, y_vals)

region = (X > 0) & (X < 4) & (Y > 0) & (Y < 4) & (Y > X - 1) & (Y < X + 1)

plt.figure(figsize=(8, 6))
plt.contourf(X, Y, region, levels=1, colors=['lightblue'], alpha=0.5)
plt.title('Región de integración para f(x, y)')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.show()
