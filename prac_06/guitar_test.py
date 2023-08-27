from prac_06.guitar import Guitar
THIS_YEAR = 2023


def main():
    guitar = Guitar("Gibson L-5 CES", 1923, 10000)
    another = Guitar("Another Guitar", 2013, 10000)
    print(f"{guitar.name} get_age() - Expected {100}. Got {guitar.get_age()}")
    print(f"{another.name} get_age() - Expected {9}. Got {another.get_age()}")
    print(f"{guitar}")
    print(f"{guitar.name} is_vintage() - Expected {True}. Got {guitar.is_vintage()}")
    print(f"{another.name} is_vintage() - Expected {False}. Got {another.is_vintage()}")


main()
