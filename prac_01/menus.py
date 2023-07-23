name = str(input("Enter name: "))
print("(H)ello\n(G)oodbye\n(Q)uit")
choice = str(input("")).upper()
while choice != "Q":
    if choice == "H":
        print(f"Hello {name}")
        choice = str(input("")).upper()
    elif choice == "G":
        print(f"Goodbye {name}")
        choice = str(input("")).upper()
    else:
        print("Invalid choice")
        print("(H)ello\n(G)oodbye\n(Q)uit")
        choice = str(input("")).upper()
print("Finished.")
