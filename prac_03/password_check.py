"""
Password Check

Created by Steven, 24-11-2021
"""

MINIMUM_LENGTH = 4


def main():
    """Get a password of at least a certain length and print asterisks."""
    password = input(f"Enter a password that is at least {MINIMUM_LENGTH} characters long: ")
    while len(password) < MINIMUM_LENGTH:
        password = input(f"Enter a password that is at least {MINIMUM_LENGTH} characters long: ")
    print('*' * len(password))


main()
