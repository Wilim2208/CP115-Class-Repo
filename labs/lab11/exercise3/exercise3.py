number = int(input())

current = 0
previous = 0
count = 0
while number != 0:
    count += number
    current += count
    if current > previous:
        biggest_jump = current
    else:
        biggest_jump = previous
    number = int(input())

print(count)
print(biggest_jump)
