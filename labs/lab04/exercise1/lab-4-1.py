kWh = float(input())
if kWh >= 100:
    if kWh > 200:
        totalBill = kWh * 0.75
    else:
        totalBill = kWh * 0.5
else:
    totalBill = kWh * 0.3
print(totalBill)
