import sys
import random
from pyfiglet import Figlet

figlet = Figlet()
fonts = figlet.getFonts()

# Validate command-line arguments
if len(sys.argv) == 1:
    # No arguments: use random font
    font = random.choice(fonts)
elif len(sys.argv) == 3 and sys.argv[1] in ["-f", "--font"]:
    font = sys.argv[2]
    if font not in fonts:
        sys.exit("Invalid font name.")
else:
    sys.exit("Usage: python figlet.py [-f FONTNAME]")

# Set the font
figlet.setFont(font=font)

# Prompt user for input
text = input("Input: ")

# Render and print text
print(figlet.renderText(text))
