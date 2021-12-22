from prac_06.guitar import Guitar


def main():
    guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
    guitar_2 = Guitar("Another Guitar", 2013, 9000)

    print(f"{guitar.name} get_age() - Expected 99. Got {guitar.get_age()}")
    print(f"{guitar_2.name} get_age() - Expected 8. Got {guitar_2.get_age()}")
    print(f"{guitar.name} is_vintage() - Expected True. Got {guitar.is_vintage()}")
    print(f"{guitar_2.name} is_vintage() - Expected False. Got {guitar_2.is_vintage()}")


main()
