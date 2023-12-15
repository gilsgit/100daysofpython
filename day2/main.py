print("Welcome to the tip calculator.")
bill = input("What was the total bill? $")
tip = input("What percentage tip would you like to give? 10, 12, or 15? ")
total_people = input("How many people to split the bill? ")

total = float(bill)
tip_total = float(tip)
amount_of_people = int(total_people)

total_to_pay = (((total * (1 + tip_total / 100)) / amount_of_people))

final_total = (round(total_to_pay, 2))

print(f"Each person should pay ${final_total}")