def main():
    while True:
        fraction = input("Fraction: ")
        try:
            x, y = fraction.split("/")
            x = int(x)
            y = int(y)

            if y == 0 or x > y:
                raise ValueError

            percentage = round((x / y) * 100)

            if percentage <= 1:
                print("E")
            elif percentage >= 99:
                print("F")
            else:
                print(f"{percentage}%")
            break  # Exit loop after valid output

        except (ValueError, ZeroDivisionError):
            # Just re-prompt if invalid
            pass


main()
