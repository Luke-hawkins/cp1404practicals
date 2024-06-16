def main():
    """Gets list of numbers from user"""
    TOTAL_INPUT_NUMBERS = 5
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']
    numbers = get_numbers(TOTAL_INPUT_NUMBERS)
    display_numbers_summary(numbers)

def get_numbers(TOTAL_INPUT_NUMBERS):
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

main()