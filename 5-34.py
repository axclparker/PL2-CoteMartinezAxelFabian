import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

x, y, c = sp.symbols('x y c')

f_xy = c * x * y

integral = sp.integrate(sp.integrate(f_xy, (x, 0, 3)), (y, 0, 3))
c_value = sp.solve(integral - 1, c)[0]
print(f"Constante de normalización c = {c_value}")

f_xy = c_value * x * y

X = np.linspace(0, 3, 100)
Y = np.linspace(0, 3, 100)
X, Y = np.meshgrid(X, Y)
Z = c_value * X * Y

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')
ax.set_title('Función de Densidad Conjunta (Ejercicio 5.34)')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('f(X, Y)')

plt.show()
