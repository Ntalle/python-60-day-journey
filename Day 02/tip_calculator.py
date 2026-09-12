print("Welcome to the Tip Calculator")
total_bill = float(input("What was your total bill: "))
tip = int(input("How much percentage tip would you like to give 10, 12, or 15 "))
split_number = int(input("How many people to split the bill? "))

total_bill_with_tip = float(round(((total_bill * tip) / 100), 2) + total_bill)

total_bill_split = float(round(total_bill_with_tip / split_number, 2))

print(f"Each person should pay {total_bill_split}.")