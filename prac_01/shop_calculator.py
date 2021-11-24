item_amount = int(input("Number of items: "))
while item_amount < 0:
    print("Invalid number of items!")
    item_amount = int(input("Number of items: "))

total = 0
for i in range(item_amount):
    price = float(input("Price of item: "))
    total += price
if total > 100:
    total *= 0.9

print(f"Total price for {item_amount} items is ${total:.2f}")
