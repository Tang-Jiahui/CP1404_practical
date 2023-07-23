# a
for i in range(0, 101, 10):
    print(i, end=' ')
print()

# b
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# c
starts = int(input("Number of stars: "))
for i in range(0, starts, 1):
    print("*", end='')
print()

# d
starts = int(input("Number of stars: "))
for i in range(0, starts, 1):
    for l in range(0, i + 1, 1):
        print("*", end='')
    print()
