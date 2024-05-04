import sympy as sp

# Define symbols
x = sp.Symbol('x')
y = sp.Function('y')(x)

# Define the ODE
ode = sp.diff(y, x, x) + 4*sp.diff(y, x) + 9*y

# Solve the ODE symbolically
solution = sp.dsolve(ode, y)

# Print the solution
print("Analytical Solution:")
print(solution)
