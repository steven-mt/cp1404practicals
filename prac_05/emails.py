"""
CP1404 Practical 5 - emails.py
Store emails and names in a dictionary
"""


def main():
    """Get emails and names from user and store them in a dictionary"""
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        email_split = email.split("@")
        name = get_name(email_split[0])

        name_check = input(f"Is your name {name}? (Y/n) ").lower()
        if name_check != "y" and name_check != "":
            name = input("Name: ")

        email_to_name[email] = name
        email = input("Email: ")
    print()
    for key, value in email_to_name.items():
        print(f"{value} ({key})")


def get_name(email_part):
    """Get name from email"""
    name = email_part.split(".")
    name = " ".join(name)
    name = name.title()
    return name


main()
