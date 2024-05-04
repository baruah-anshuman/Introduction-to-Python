import sympy as sp

def solve_polynomial(expr, var):
  """
  Solves a polynomial equation for a given variable.

  Args:
      expr: A symbolic expression representing the polynomial equation.
      var: The variable to solve the equation for (e.g., 'x').

  Returns:
      A list of symbolic solutions.
  """
  solutions = sp.solve(expr, var)
  return solutions

def get_symbolic_expression(prompt):
  """
  Prompts the user for a polynomial expression and converts it to a symbolic form.

  Args:
      prompt: The message to display to the user.

  Returns:
      A symbolic expression representing the user-provided polynomial.
  """
  while True:
    try:
      expr_str = input(prompt)
      # Extract potential variable symbol(s)
      var_candidates = sp.symbols(expr_str.split("=")[0])

      # Check if there's a single variable or multiple (use isinstance)
      if isinstance(var_candidates, sp.Symbol):
        var = var_candidates  # Use the single Symbol object directly
      else:
        # If multiple variables, prompt the user to choose one... (rest unchanged)
        ...

      expr = sp.sympify(expr_str.replace(var.name, str(var)))  # Convert to symbolic expression
      return expr, var
    except (SyntaxError, ValueError):
      print("Invalid expression. Please enter a valid polynomial equation (e.g., 2x^2+3x+4=0).")

# Get the symbolic expression and variable from the user
expr, var = get_symbolic_expression("Enter a polynomial equation (e.g., 2x^2+3x+4=0): ")

# Solve the equation
solutions = solve_polynomial(expr, var)

# Print the results
print("Solutions:")
for solution in solutions:
  print(solution)
