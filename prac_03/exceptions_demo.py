"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
    When the numerator or denominator are not a valid number, like the input have the symbols and letters
2. When will a ZeroDivisionError occur?
    When the number which is divided is equal to 0 in the division.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
    I think we can make a program like the valid input check to make sure the user do not enter 0 for the denominator.
"""

ZERO = 0

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == ZERO:
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")