import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

x, y, c = sp.symbols('x y c')

f_xy = c * x * y

integral_c = sp.integrate(sp.integrate(f_xy, (x, 0, 3)), (y, 0, 3))
c_value = sp.solve(integral_c - 1, c)[0]  
print(f"Constante de normalización c = {c_value}")

f_xy = f_xy.subs(c, c_value)

# a. Distribución marginal de X
f_x = sp.integrate(f_xy, (y, 0, 3))
print(f"Distribución marginal de X: f_X(x) = {f_x}")

# b. Distribución marginal de Y
f_y = sp.integrate(f_xy, (x, 0, 3))
print(f"Distribución marginal de Y: f_Y(y) = {f_y}")

# c. Distribución condicional de Y dado X=1.5
f_y_given_x = f_xy / f_x
f_y_given_x_at_1_5 = f_y_given_x.subs(x, 1.5)
print(f"Distribución condicional de Y dado X=1.5: f_Y|X(y|1.5) = {f_y_given_x_at_1_5}")

# d. Distribución condicional de X dado Y=2
f_x_given_y = f_xy / f_y
f_x_given_y_at_2 = f_x_given_y.subs(y, 2)
print(f"Distribución condicional de X dado Y=2: f_X|Y(x|2) = {f_x_given_y_at_2}")

# Marginal de X
x_vals = np.linspace(0, 3, 100)
f_x_numeric = sp.lambdify(x, f_x, "numpy")
plt.figure()
plt.plot(x_vals, f_x_numeric(x_vals), label="f_X(x)")
plt.title("Distribución marginal de X")
plt.xlabel("x")
plt.ylabel("f_X(x)")
plt.legend()
plt.grid()

# Marginal de Y
y_vals = np.linspace(0, 3, 100)
f_y_numeric = sp.lambdify(y, f_y, "numpy")
plt.figure()
plt.plot(y_vals, f_y_numeric(y_vals), label="f_Y(y)")
plt.title("Distribución marginal de Y")
plt.xlabel("y")
plt.ylabel("f_Y(y)")
plt.legend()
plt.grid()

# Condicional de Y dado X=1.5
f_y_given_x_numeric = sp.lambdify(y, f_y_given_x_at_1_5, "numpy")
plt.figure()
plt.plot(y_vals, f_y_given_x_numeric(y_vals), label="f_Y|X(y|1.5)")
plt.title("Distribución condicional de Y dado X=1.5")
plt.xlabel("y")
plt.ylabel("f_Y|X(y|1.5)")
plt.legend()
plt.grid()

# Condicional de X dado Y=2
f_x_given_y_numeric = sp.lambdify(x, f_x_given_y_at_2, "numpy")
plt.figure()
plt.plot(x_vals, f_x_given_y_numeric(x_vals), label="f_X|Y(x|2)")
plt.title("Distribución condicional de X dado Y=2")
plt.xlabel("x")
plt.ylabel("f_X|Y(x|2)")
plt.legend()
plt.grid()

plt.show()
