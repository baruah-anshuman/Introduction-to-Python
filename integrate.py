import scipy.integrate

# Define the function to integrate
def func(x):
    return x**2

# Integrate the function from 0 to 1
result, error = scipy.integrate.quad(func, 0, 1)
print("Result of integration:", result)
print("Estimated error:", error)