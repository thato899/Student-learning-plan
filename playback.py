userString = input("Please enter your string: ")

def playback(userString):
    newString = userString.replace(" ", "...")
    return newString

print(playback(userString))
