"""
Word Occurrences
Estimate: 10 minutes
Actual:   5 minutes
"""

THIS_YEAR = 2023
VINTAGE_AGE = 50


class Guitar:
    def __init__(self, name, year, cost):
        """make sure the elements"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """make a information collection"""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """get guitar's age"""
        return THIS_YEAR - self.year

    def is_vintage(self):
        """make sure the age is in vintage age or not"""
        if self.get_age() >= VINTAGE_AGE:
            return True
        else:
            return False
