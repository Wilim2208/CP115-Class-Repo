grade = float(input())

total = 0
valid_count = 0
while grade != -1:
    if (grade >= 0) and (grade <= 100):
        total += grade
        valid_count += 1
        grade = float(input())
    else:
        grade = float(input())
        continue

average = total / valid_count
print(valid_count)
print(f"{average:.2f}")
