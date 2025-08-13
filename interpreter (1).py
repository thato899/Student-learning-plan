# interpreter.py

# Prompt the user for an arithmetic expression
expression = input("Expression: ")

# Split the input into its parts: x, operator, z
x_str, operator, z_str = expression.split()

# Convert numbers from string to integer
x = int(x_str)
z = int(z_str)

# Perform the calculation based on the operator
if operator == "+":
    result = x + z
elif operator == "-":
    result = x - z
elif operator == "*":
    result = x * z
elif operator == "/":
    if z!=0:
        result = x / z
else:
    print("Unknown operator")
    exit()

# Output the result formatted to one decimal place
print(f"{result:.1f}")
