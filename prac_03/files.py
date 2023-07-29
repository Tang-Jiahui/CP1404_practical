#1
NAME_FILE = "name.txt"

name_file = open(NAME_FILE, 'w')
name = str(input("Please enter a name:"))
name_file.write(name)
name_file.close

#2
name_file = open(NAME_FILE, 'r')
output_name = name_file.read()
print(f"Your name is {output_name}")
name_file.close

#3
