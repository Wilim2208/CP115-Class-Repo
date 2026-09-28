#willieam
#calculating the amount of bill to be pay
usage = float(input("Enter monthly usage :RM ")) #user enter their monthly usage

if usage < 50: #monthly usage less than RM50
    paid_amount = usage
elif usage <= 100: #monthly usage less than or equal to RM100
    paid_amount = usage - (usage * 0.05)
else: #monthly usage more then RM100
    paid_amount = usage - (usage * 0.2)
print(f"Total amount to pay is RM{paid_amount: .2f}")
