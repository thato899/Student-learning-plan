import emoji

# Prompt user for input
text = input("Input: ")

# Convert codes and aliases to emojis
emojized_text = emoji.emojize(text, language="alias")

# Output result
print("Output:", emojized_text)

