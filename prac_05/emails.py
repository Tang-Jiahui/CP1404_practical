"""
Word Occurrences
Estimate: 10 minutes
Actual:   15 minutes
"""

emails = {}
input_email = input("Email:")
while input_email != "":
    provisional_name = input_email.split('@')[0]
    prepare_name = provisional_name.split('.')
    name = " ".join(prepare_name).title()
    confirm_name = input(f"Is your name {name}? (Y/n)").upper()
    if confirm_name.upper() != "Y" and confirm_name != "":
        name = input("Name:")
    emails[input_email] = name
    input_email = input("Email:")

for i in range(0, len(emails)):
    print(f"{list(emails.values())[i]} ({list(emails.keys())[i]})")