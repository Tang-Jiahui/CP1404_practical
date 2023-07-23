"""Score"""
import random


def main():
    """Main function"""
    MINIMUM = 0
    MAXIMUM = 100
    PASSABLE = 50
    EXCELLENT = 90
    score = float(input("Enter score: "))
    result = get_result(EXCELLENT, MAXIMUM, MINIMUM, PASSABLE, score)
    print(result)
    random_score = random.randint(1, 100)
    random_result = get_result(EXCELLENT, MAXIMUM, MINIMUM, PASSABLE, random_score)
    print(random_result)


def get_result(EXCELLENT, MAXIMUM, MINIMUM, PASSABLE, score):
    """Calculate the result by score"""
    if score < MINIMUM:
        return "Invalid score"
    elif score > MAXIMUM:
        return "Invalid score"
    else:
        if score < PASSABLE:
            return "Bad"
        elif score <= EXCELLENT:
            return "Passable"
        else:
            return "Excellent"


main()
