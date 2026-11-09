
print("welcome to CATUC Shoping With discount")
num_items = int(input("please enter how many items you bought:\n"))
items_cost = []
for items in range(1,num_items + 1):
    cost =float(input(f"please enter cost of item {items}:\n"))
    items_cost.append(cost)
    
items_cost_total = sum(items_cost)
if items_cost_total > 5000:
    discount = 0.10 * items_cost_total
    total_cost = items_cost_total - discount
    print(f" total purchase ={total_cost} frs\n Thanks for your patronage ")
elif (len(items_cost) >= 5) and (items_cost_total > 4000):
    discount = 0.15 * items_cost_total
    total_cost = items_cost_total - discount
    print(f"Total purchase = {total_cost} frs\n Thanks for your patronage")
elif items_cost_total > 5000:
    discount = 0.10 * items_cost_total
    total_cost = items_cost_total - discount
    print(f"Total purchase = {total_cost} frs\n Thanks for your patronage")
else:
    total_cost = items_cost_total
    print(f"total purchase = {total_cost}frs\nThanks for your patronage")
print("\n CATUC SHPING RECEIPT ")
for items,cost in enumerate(items_cost, start=1):
    print(f"items{items}: {cost:,.1f} frs")
    
print(f"total cost:{items_cost_total:,.1f}frs")
print(f"Discount:{discount:,.1f}frs")
print(f"total price paid:{total_cost:,.1f}frs")
print("Thank you for shopping at CATUC see you next time👋")
