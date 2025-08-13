userInput = int(input("Please enter mass in kg: "))

def einstein(userInput):
    c = 300000000
    E = userInput * c**2
    return E

print(einstein(userInput))
