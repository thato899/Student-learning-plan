
def convert(inputString):
    inputString = inputString.replace(":)", "🙂")
    inputString = inputString.replace(":(", "🙁")
    return inputString

def main():
    inputString = input("Please enter your string: ")
    converted = convert(inputString)
    print(converted)

main()

