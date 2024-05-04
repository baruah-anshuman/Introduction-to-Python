import sympy as sp

def main():
    # Define the symbols
    x, y = sp.symbols('x y')
    
    # Prompt the user to input the function
    function_str = input("Enter the function to integrate: ")

    # Create the function object
    function = eval(function_str, {**vars(sp), 'x': x, 'y': y})

    # Prompt the user to input the variable for integration
    variable_str = input("Enter the variable for integration: ")
    integration_variable = sp.Symbol(variable_str)

    # Integrate the function with respect to the specified variable
    integral = sp.integrate(function, integration_variable)

    # Print the result
    print(f"Integral of the function with respect to {integration_variable}:")
    print(integral)

if __name__ == "__main__":
    main()
