# Basic list operations
MIN_TIMES = 0
MAX_TIMES = 5
number = []
for i in range(MIN_TIMES, MAX_TIMES):
    input_number = int(input("Number:"))
    number.append(input_number)
    i += 1
average_numbers = sum(number) / len(number)
print(f"The first number is {number[0]}")
print(f"The last number is {number[-1]}")
print(f"The smallest number is {min(number)}")
print(f"The largest number is {max(number)}")
print(f"The average of the number is {average_numbers}")

# Woefully inadequate security checker
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
username_input = str(input("Please enter username:"))
if username_input in usernames:
    print("Access granted")
else:
    print("Access denied")
