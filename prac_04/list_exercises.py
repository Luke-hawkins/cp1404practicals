TOTAL_INPUT_NUMBERS = 5
def main():
    """Gets list of numbers from user"""
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']
    numbers = get_numbers()
    display_numbers_summary(numbers)
    username = str(input("Username: "))
    check_username(usernames, username)

def get_numbers():
    """Gets numbers from uses depending on TOTAL_INPUT_NUMBERS"""
    numbers = []
    while len(numbers) != TOTAL_INPUT_NUMBERS:
        numbers.append(int(input("Number: ")))
    return numbers

def display_numbers_summary(numbers):
    """display overview of numbers in numbers list"""
    sorted_numbers = sorted(numbers)
    print(f"The first number is {numbers[0]} \nThe last number is {numbers[-1]} \n"
          f"The smallest number is {sorted_numbers[0]} \nThe largest number is {sorted_numbers[-1]}\n"
          f"The average of the numbers is {sum(numbers) / len(numbers)}")

def check_username(usernames, username):
    """check if username is in usernames list"""
    if username in usernames:
        print("Access granted")
    else:
        print("access denied")


main()