import math

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

# Example usage
a = 1
b = 5
c = 6
roots = solve_quadratic(a, b, c)

for root in roots:
  if isinstance(root, complex):
    print("The equation has an imaginary root:", root)
  else:
    print("The equation has a real root:", root)
