import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

x, y, c = sp.symbols('x y c')

f_xy_5_37 = c * (x + y)

integral_5_37 = sp.integrate(sp.integrate(f_xy_5_37, (y, 0, x + 2)), (x, 0, 3))
c_value_5_37 = sp.solve(integral_5_37 - 1, c)[0]
print(f"Constante de normalización c (5.37 y 5.38) = {c_value_5_37}")

f_xy = c_value_5_37 * (x + y)  

# a) P(X < 1, Y < 2)
prob_5_38_a = sp.integrate(sp.integrate(f_xy, (y, 0, x + 2)), (x, 0, 1))
print(f"P(X < 1, Y < 2) = {prob_5_38_a}")

# b) P(1 < X < 2)
prob_5_38_b = sp.integrate(sp.integrate(f_xy, (y, 0, x + 2)), (x, 1, 2))
print(f"P(1 < X < 2) = {prob_5_38_b}")

# c) P(Y > 2)
prob_5_38_c = sp.integrate(sp.integrate(f_xy, (x, 0, 3)), (y, 2, x + 2))
print(f"P(Y > 2) = {prob_5_38_c}")

# d) P(X < 2, Y < 2)
prob_5_38_d = sp.integrate(sp.integrate(f_xy, (y, 0, 2)), (x, 0, 2))
print(f"P(X < 2, Y < 2) = {prob_5_38_d}")

E_X = sp.integrate(sp.integrate(x * f_xy, (y, 0, x + 2)), (x, 0, 3))
E_Y = sp.integrate(sp.integrate(y * f_xy, (y, 0, x + 2)), (x, 0, 3))
print(f"Esperanza E(X) = {E_X}")
print(f"Esperanza E(Y) = {E_Y}")

X_vals = np.linspace(0, 3, 100)
Y_vals = np.linspace(0, 5, 100)
X_vals, Y_vals = np.meshgrid(X_vals, Y_vals)
Z_vals = c_value_5_37 * (X_vals + Y_vals)

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X_vals, Y_vals, Z_vals, cmap='viridis')
ax.set_title('Función de Densidad Conjunta (Ejercicio 5.38)')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('f(X, Y)')
plt.show()

plt.figure(figsize=(8, 6))
plt.contourf(X_vals, Y_vals, Z_vals, levels=20, cmap='viridis')
plt.colorbar(label='Densidad')
plt.title('Contorno de la Función de Densidad Conjunta (Ejercicio 5.38)')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.show()
