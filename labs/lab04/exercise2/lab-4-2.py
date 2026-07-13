income = float(input())
if income > 50000:
    if income > 100000:
        totalTax = income + income * 0.2
    else:
        totalTax = income + income * 0.1
else:
    totalTax = income
print(totalTax)
