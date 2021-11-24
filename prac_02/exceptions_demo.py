"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

# 1. A ValueError will occur when the user does not input an integer.
# 2. A ZeroDivisionError will occur when the user inputs a zero as the denominator.

try:
    numerator = int(input("Enter the numerator: "))

    # 3. while loop using exceptions to avoid ZeroDivisionError
    valid_input = False
    while not valid_input:
        try:
            denominator = int(input("Enter the denominator: "))
            fraction = numerator / denominator
            valid_input = True
            print(fraction)
        except ZeroDivisionError:
            print("Denominator cannot be zero.")

except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")
