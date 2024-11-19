import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

x, y, c = sp.symbols('x y c')

f_xy_5_37 = c * (x + y)

integral_5_37 = sp.integrate(sp.integrate(f_xy_5_37, (y, x, x + 2)),
                             (x, 0, 3))

c_value_5_37 = sp.solve(integral_5_37 - 1, c)[0]
print(f"Constante de normalización c (5.37) = {c_value_5_37}")

f_xy_5_37 = c_value_5_37 * (x + y)

X = np.linspace(0, 3, 100)
Y = np.linspace(0, 5, 100)  
X, Y = np.meshgrid(X, Y)
Z_5_37 = np.zeros_like(X)

for i in range(len(X)):
    for j in range(len(Y)):
        if 0 < X[i, j] < 3 and X[i, j] < Y[i, j] < X[i, j] + 2:
            Z_5_37[i, j] = c_value_5_37 * (X[i, j] + Y[i, j])

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z_5_37, cmap='viridis')
ax.set_title('Función de Densidad Conjunta (Ejercicio 5.37)')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('f(X, Y)')
plt.show()
