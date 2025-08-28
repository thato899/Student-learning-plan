import random

# Prompt user for level
while True:
    try:
        level = int(input("Level: "))
        if level > 0:
            break
    except ValueError:
        continue  # Not an integer, ask again

# Generate a random number between 1 and level
secret = random.randint(1, level)

# Keep asking for guesses
while True:
    try:
        guess = int(input("Guess: "))
        if guess <= 0:
            continue  # Ignore non-positive guesses

        if guess < secret:
            print("Too small!")
        elif guess > secret:
            print("Too large!")
        else:
            print("Just right!")
            break
    except ValueError:
        continue  # Ignore non-integers
