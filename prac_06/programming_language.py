"""
Word Occurrences
Estimate: 15 minutes
Actual:   15 minutes
"""

class ProgrammingLanguage:
    def __init__(self, name, typing, reflection, year):
        """make sure the elements"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """display the dynamic"""
        return self.typing == "Dynamic"

    def __str__(self):
        """display the collected information"""
        return f"{self.name}, {self.typing}, Reflection={self.reflection}, First appeared in {self.year}"

