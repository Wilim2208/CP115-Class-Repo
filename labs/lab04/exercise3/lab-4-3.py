hour = int(input())
if hour > 2:
    if hour > 5:
        parkingFee = hour * 3
    else:
        parkingFee = hour * 2
else:
    parkingFee = 0
if parkingFee > 30:
    capped = 30
    print(capped)
else:
    print(parkingFee)
