def main():
    MIN_NAME = 6
    password = get_password(MIN_NAME)
    print_password(password)


def print_password(password):
    for i in range(0, len(password)):
        print("*", end="")
        i += 1


def get_password(MIN_NAME):
    password = str(input("Please enter password:"))
    while len(password) < MIN_NAME:
        password = str(input("Please enter password:"))
    return password


main()
