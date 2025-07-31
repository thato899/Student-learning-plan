#Write a palindrome checker that tells if a word is the same forward and backward.
word = input("Please type in your word: ")
new_word = word[: : -1]
if word == new_word:
    print("This is a pelendrome")
else:
    print(" The word is not a pelendrome.")