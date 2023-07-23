total = 0
number_of_items = int(input("Number of items:"))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items:"))
for i in range(0, number_of_items, 1):
    price = float(input("Price of item:"))
    total += price
if total > 100:
    final_total = total * 0.9
    print(f"Total price for {number_of_items} items is ${final_total}")
else:
    final_total = total
    print(f"Total price for {number_of_items} items is ${final_total}")