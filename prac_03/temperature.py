"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""


def celsius_to_fahrenheit(celsius):
    """Convert celsius to fahrenheit."""
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


def fahrenheit_to_celsius(fahrenheit):
    """Convert fahrenheit to celsius."""
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


def main():
    """Gets a choice from the user and then converts the temperature inputs accordingly."""
    MENU = """C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = celsius_to_fahrenheit(celsius)
            print("Result: {:.2f} F".format(fahrenheit))
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            celsius = fahrenheit_to_celsius(fahrenheit)
            print(f"Result: {celsius:.2f}")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")
