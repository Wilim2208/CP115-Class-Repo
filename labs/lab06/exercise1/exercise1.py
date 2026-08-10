muffin = 3 * 2.10
coffee = 2 * 3.50
water = 4 * 1.05
subtotal = muffin + coffee + water 
tax = 1.05
total = subtotal + tax
print(f"============== RECEIPT ==============\nItem\t\tPrice\tQty\tTotal\nCoffee\t\t$3.50\t2\t$7.00\nMuffin\t\t$2.10\t3\t$6.30\nWater\t\t$1.05\t4\t$4.20\n-------------------------------------\nSubtotal\t\t${subtotal}\nTax(6%)\t\t\t${tax}\nTotal\t\t${total}\n=====================================")