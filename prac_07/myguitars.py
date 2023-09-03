from guitar import Guitar


def main():
    """main function"""
    guitars = []
    in_file = open('guitars.csv', 'r')
    for line in in_file.readlines():
        parts = line.strip().split(',')
        parts[2] = float(parts[2])
        guitar = Guitar(parts[0], parts[1], parts[2])
        guitars.append(guitar)

    in_file.close()
    sorted_guitar_list = []
    sorted_guitars = sorted(guitars)
    for sorted_guitar in sorted_guitars:
        print(sorted_guitar)

    for i in range(0, len(sorted_guitars)):
        sorted_guitars[i] = str(sorted_guitars[i])
        sorted_guitar_list.append(sorted_guitars[i])
    new_guitar_file = open("guitars.csv", "w")
    for line in range(0, len(sorted_guitar_list)):
        new_guitar_file.writelines(sorted_guitar_list[line])
        new_guitar_file.writelines("\n")
    new_guitar_file.close()


if __name__ == '__main__':
    main()
