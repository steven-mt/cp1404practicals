"""
Password Check

Created by Steven, 24-11-2021
"""

MINIMUM_LENGTH = 4


def main():
    """Get a password of at least a certain length and print asterisks."""
    password = get_password()
    display_asterisk(password)


def get_password():
    """Get password from the user with error checking."""
    password = input(f"Enter a password that is at least {MINIMUM_LENGTH} characters long: ")
    while len(password) < MINIMUM_LENGTH:
        password = input(f"Enter a password that is at least {MINIMUM_LENGTH} characters long: ")
    return password


def display_asterisk(password):
    """Print as many asterisks as the length of the password to the screen."""
    print('*' * len(password))


main()
