#Tip Calculator 
print("Welcome to the tip calculator.\n")

total_bill = float(input("What was the total bill? $"))

percent_tip = int(input("What percent of tip would you like to give? 10, 12, or 15? ")) / 100

people_bill_split = int(input("How many people to split the bill? "))

bill = total_bill * percent_tip + total_bill
bill_each = round(bill / people_bill_split, 2)

print(f"Each person should pay: ${bill_each}")