import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Define the second-order ODE
def f(x, y):
    return [y[1], -4*y[1] - 9*y[0]]

# Define the initial conditions
y0 = [1, 0]  # initial values of y and dy/dx

# Define the range of x values for the solution
x_span = (0, 10)

# Solve the ODE
sol = solve_ivp(f, x_span, y0, t_eval=np.linspace(0, 10, 100))

# Plot the solution
plt.plot(sol.t, sol.y[0], label='y(x)')
plt.plot(sol.t, sol.y[1], label="y'(x)")
plt.xlabel('x')
plt.ylabel('y(x), y\'(x)')
plt.title('Numerical Solution of the Second-Order ODE')
plt.legend()
plt.grid(True)
plt.show()