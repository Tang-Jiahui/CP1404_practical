import random

NUMBERS_OF_LINE = 6
MIN_NUMBER = 1
MAX_NUMBER = 45

pick_numbers = int(input("How many picks? "))
for i in range(0, pick_numbers):
    pick = []
    for numbers in range(0, NUMBERS_OF_LINE):
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        while number in pick:
            number = random.randint(MIN_NUMBER, MAX_NUMBER)
        pick.append(number)
    pick.sort()
    print(" ".join(f"{number:2}" for number in pick))
