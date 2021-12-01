import random

NUMBERS_PER_LINE = 6
MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 45

number_of_quick_picks = int(input("How many quick picks? "))
for i in range(number_of_quick_picks):
    quick_pick = []
    for j in range(NUMBERS_PER_LINE):
        number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
        while number in quick_pick:
            number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
        quick_pick.append(number)
    quick_pick.sort()
    for number in quick_pick:
        print(f"{number:2}", end=" ")
    print()