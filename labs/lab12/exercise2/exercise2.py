number = 1
while number <= 100:
    if (number % 7 == 0) and (number % 13 == 0):
        found_number = number
        break   
print(found_number)
