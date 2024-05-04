import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

# Define the symbol
x = sp.Symbol('x')

# Define the function to integrate
func = 1 / (x ** 2)

# Integrate the function symbolically
integral = sp.integrate(func, (x, 1, sp.oo))  # Integrate from 1 to infinity

print("Symbolic integral:", integral)

# Plot the function
x_vals = np.linspace(1, 10, 1000)
y_vals = 1 / (x_vals ** 2)

plt.plot(x_vals, y_vals, label=r'$\frac{1}{x^2}$')
plt.fill_between(x_vals, y_vals, color='skyblue', alpha=0.4)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Plot of the function f(x) = 1/x^2')
plt.grid(True)
plt.legend()
plt.show()
