"""
CP1404/CP5632 - Practical
Password checker "skeleton" code to help you get started
"""

"""I changed the program to use True or False instead of a count as it required less
code and the total number of each characters was irrelevant. just needed to know if it was of was not included
"""

MIN_LENGTH = 2
MAX_LENGTH = 6
IS_SPECIAL_CHARACTER_REQUIRED = False
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    """Program to get and check a user's password."""
    print("Please enter a valid password")
    print(f"Your password must be between {MIN_LENGTH} and {MAX_LENGTH} characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if IS_SPECIAL_CHARACTER_REQUIRED:
        print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print(f"Your {len(password)}-character password is valid: {password}")

def is_valid_password(password):
    """Determine if the provided password is valid."""
    if len(password) < MIN_LENGTH or len(password) > MAX_LENGTH:
        return False

    # Checks different types of character and changes variables to True.
    lower_character = False
    upper_character = False
    digit_character = False
    special_character = False
    for character in password:
        if character.islower():
            lower_character = True
        elif character.isupper():
            upper_character = True
        elif character.isdigit():
            digit_character = True
        elif character in SPECIAL_CHARACTERS:
            special_character = True
        else: # if no conditions are true an invalid character was inputted
            return False

    # checks to see if any conditions are false
    if IS_SPECIAL_CHARACTER_REQUIRED:
        if not(lower_character and upper_character and digit_character and special_character):
            return False
    else:
        if not (lower_character and upper_character and digit_character):
            return False

    # if code made it this far password is valid
    return True


main()