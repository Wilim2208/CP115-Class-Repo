ticketPrice = float(input())
baggage = float(input())
if baggage > 15:
    charge = baggage - 15 * 4
    finalPrice = charge + ticketPrice
else:
    if baggage <= 0:
        finalPrice = ticketPrice - 10
    else:
        finalPrice = ticketPrice
print(finalPrice)
