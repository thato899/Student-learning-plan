import inflect

# Create an inflect engine
p = inflect.engine()

# Collect names until EOF (Ctrl-D / Ctrl-Z)
names = []
try:
    while True:
        name = input("Name: ")
        names.append(name)
except EOFError:
    print()  # Move to a new line after Ctrl-D

# Join names with commas and 'and'
joined_names = p.join(names)

# Print final message
print(f"Adieu, adieu, to {joined_names}")
