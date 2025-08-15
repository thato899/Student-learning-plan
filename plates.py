def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    return (
        has_valid_length(s)
        and starts_with_two_letters(s)
        and numbers_at_end_only(s)
        and no_illegal_chars(s)
    )


def has_valid_length(s):
    return 2 <= len(s) <= 6


def starts_with_two_letters(s):
    return s[0:2].isalpha()


def numbers_at_end_only(s):
    """Check that if there are numbers, they appear only at the end,
       first number not '0'."""
    for i, char in enumerate(s):
        if char.isdigit():
            # First digit can't be '0'
            if char == '0':
                return False
            # Everything after the first digit must be digits
            return s[i:].isdigit()
    return True  # No numbers at all


def no_illegal_chars(s):
    return s.isalnum()


main()

