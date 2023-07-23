"""Score_menu"""


def main():
    """Main function"""
    MINIMUM = 0
    MAXIMUM = 100
    PASSABLE = 50
    EXCELLENT = 90
    MENU = """(G)et a valid score
(P)rint result
(S)how stars
(Q)uit"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_score(MAXIMUM, MINIMUM)
        elif choice == "P":
            result = get_result(EXCELLENT, PASSABLE, score)
            print(result)
        elif choice == "S":
            show_stars(score)
            print("")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def show_stars(score):
    """Translate the score by *"""
    for i in range(0, score):
        print("*", end="")
        i += 1


def get_result(EXCELLENT, PASSABLE, score):
    """Calculate the result by score"""
    if score < PASSABLE:
        return "Bad"
    elif score <= EXCELLENT:
        return "Passable"
    else:
        return "Excellent"


def get_score(MAXIMUM, MINIMUM):
    """Get the password and check is it valid"""
    score = int(input("Enter score: "))
    while score < MINIMUM or score > MAXIMUM:
        score = int(input("Enter score: "))
    return score


main()
