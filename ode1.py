import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Define the first-order ODE
def f(t, y):
    return -2 * t * y

# Define the initial condition
y0 = 1

# Define the time points for the solution
t_span = (0, 2)

# Solve the ODE
sol = solve_ivp(f, t_span, [y0], t_eval=np.linspace(0, 2, 100))

# Plot the solution
plt.plot(sol.t, sol.y[0], label='Numerical Solution')
plt.xlabel('t')
plt.ylabel('y(t)')
plt.title('Solution of the First-Order ODE')
plt.legend()
plt.grid(True)
plt.show()