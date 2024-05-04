import math
def get_float_input(prompt):
  """
  Prompts the user for a floating-point number and validates the input.

  Args:
      prompt: The message to display to the user.

  Returns:
      A floating-point number entered by the user.
  """
  while True:
    try:
      value = float(input(prompt))
      return value
    except ValueError:
      print("Invalid input. Please enter a number.")

def solve_quadratic(a, b, c):
  """
  Solves a quadratic equation of the form ax^2 + bx + c = 0.

  Args:
      a: The coefficient of the x^2 term.
      b: The coefficient of the x term.
      c: The constant term.

  Returns:
      A tuple containing two elements:
          - The first element is a complex number representing the first root (if applicable). 
          - The second element is a complex number representing the second root (if applicable).
  """

  discriminant = b**2 - 4 * a * c
  if discriminant < 0:
    # Two imaginary roots
    real_part = -b / (2 * a)
    imaginary_part = math.sqrt(-discriminant) / (2 * a)
    root1 = complex(real_part, imaginary_part)
    root2 = complex(real_part, -imaginary_part)
    return root1, root2
  elif discriminant == 0:
    root = -b / (2 * a)
    return root, root  # One repeated real root
  else:
    root1 = (-b + math.sqrt(discriminant)) / (2 * a)
    root2 = (-b - math.sqrt(discriminant)) / (2 * a)
    return root1, root2

# Get input from the user
a = get_float_input("Enter the coefficient of the x^2 term (a): ")
b = get_float_input("Enter the coefficient of the x term (b): ")
c = get_float_input("Enter the constant term (c): ")

# Solve the equation
roots = solve_quadratic(a, b, c)

# Print the results
for root in roots:
  if isinstance(root, complex):
    print("The equation has an imaginary root:", root)
  else:
    print("The equation has a real root:", root)
