"""
Word Occurrences
Estimate: 15 minutes
Actual:   30 minutes
"""

from prac_06.guitar import Guitar
THIS_YEAR = 2023


def main():
    """get the guitars and display them"""
    guitars = []
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    name = str(input("Name: "))
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))

        add_guitar = Guitar(name, year, cost)
        guitars.append(add_guitar)
        print(f"{add_guitar} added")
        print(guitars[2].name)
        name = input("Name: ")
    for i in range(0, len(guitars)):
        print(
            f"Guitar {i + 1}: {guitars[i].name:>20} ({guitars[i].year}), worth ${guitars[i].cost:10,.2f}{guitars[i].is_vintage()}")


main()
