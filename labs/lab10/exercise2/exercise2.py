num_days = int(input())
danger_threshold = float(input())

danger_days = 0
total_tempt = 0.0

for i in range(num_days):
    tempt = float(input())
    if tempt > danger_threshold:
        danger_days += 1
    total_tempt += tempt
    average_temp = total_tempt / num_days  
    
print(danger_days)
print(f"{average_temp:.1f}")
