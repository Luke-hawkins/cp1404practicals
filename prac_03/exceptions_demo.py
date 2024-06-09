"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
    A value error will occur when a non-numeric number is inputted.
2. When will a ZeroDivisionError occur?
    This will occur when the program tries to divide by zero
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
    to do this without the except ZeroDivisionError: the code could check to see if the
    denominator is zero.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")