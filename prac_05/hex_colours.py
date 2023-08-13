"""
Word Occurrences
Estimate: 10 minutes
Actual:   12 minutes
"""

CODE_OF_COLOR = {"ABSOLUTE ZERO": "#0048ba", "ACID GREEN": "#b0bf1a", "ALICEBLUE": "#f0f8ff",
                 "ALIZARIN CRIMSON": "#e32636", "word_occurrences": "#e52b50", "AMBER": "#ffbf00", "AMETHYST": "#9966cc",
                 "ANTIQUEWHITE": "#faebd7", "ANTIQUEWHITE1": "#ffefdb", "ANTIQUEWHITE2": "#eedfcc"}
print(CODE_OF_COLOR)
color_name = str(input("Enter color's name: ")).upper()
while color_name != "":
    if color_name in CODE_OF_COLOR:
        print(color_name, "is", CODE_OF_COLOR[color_name])
    else:
        print("Invalid short state")
    color_name = str(input("Enter color's name: ")).upper()

for i in range(0, len(CODE_OF_COLOR) - 1):
    print(f"{list(CODE_OF_COLOR.keys())[i]} is {list(CODE_OF_COLOR.values())[i]}")
    i += 1
