#1
NAME_FILE = "name.txt"

name_file = open(NAME_FILE, 'w')
name = str(input("Please enter a name:"))
name_file.write(name)
name_file.close

#2
NAME_FILE = "name.txt"

name_file = open(NAME_FILE, 'r')
output_name = name_file.read()
print(f"Your name is {output_name}")
name_file.close

#3
NUMBERS = "numbers.txt"
number = open(NUMBERS, 'r')
first_number = int(number.readline())
second_number = int(number.readline())
result = first_number + second_number
print(result)
number.close

#4
NUMBERS = "numbers.txt"
number = open(NUMBERS, 'r')
total = 0
for line in number.readlines():
    line_number = int(line)
    total += line_number
print(total)
number.close