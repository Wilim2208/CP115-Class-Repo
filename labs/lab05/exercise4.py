name = str(input("Enter the item name: "))
price = float(input("Enter the price: "))
quantity = 3
tax_rate = 0.06
subtotal = price * quantity
total_cost = subtotal + subtotal * tax_rate

print(f"Your subtotal is RM{subtotal}")
print(f"The tax amount is {tax_rate}")
print(f"Your total cost is RM{total_cost}")