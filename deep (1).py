answer = input("what is the Answer to the great Question of life, the universe, and Everything? ")
def deep(answer):
    answer = answer.lower().strip()
    match answer:
        case "42":
            print("Yes")
        case "forty-two":
            print("Yes")
        case "forty two":
            print("Yes")
        case _:
            print("No")

deep(answer)
