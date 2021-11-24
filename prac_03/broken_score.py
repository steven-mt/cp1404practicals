"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


def main():
    """Get the score from the user and print the result."""
    score = float(input("Enter score: "))
    print(get_result(score))


def get_result(score):
    """Get the result from the score."""
    if score > 100 or score < 0:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
