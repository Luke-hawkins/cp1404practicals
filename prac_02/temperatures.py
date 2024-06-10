"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""


def main():
    """Displays converted units of temperature"""
    MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = convert_celsius_to_fahrenheit(celsius)
            print(f"Result: {fahrenheit:.2f} °F")
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            celsius = convert_fahrenheit_to_celsius(fahrenheit)
            print(f"Result: {celsius:.2f} °C")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")

def convert_fahrenheit_to_celsius(fahrenheit):
    """Return converted temperature from Fahrenheit to Celsius"""
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius

def convert_celsius_to_fahrenheit(celsius):
    """Return converted temperature from Celsius to Fahrenheit"""
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


main()