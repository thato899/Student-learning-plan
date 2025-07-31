#practice from the beginning of the bootcamp
#taking name as input and checking legal age
name = input("Enter your name: ")
age = int(input("Enter your age: "))

if age >= 18:
    print(f"Hello {name}, you're old enough to vote.")
else:
    print(f"Hi {name}, you're too young to vote.")
