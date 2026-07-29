print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $"))
tip = float(input("How much tip would you like to give? "))
no_people = int(input("How many people to split the bill? "))
total_bill = total_bill + (total_bill * tip/100)
bill_per_person = total_bill / no_people
final_amount = round(bill_per_person, 2)
print(f"Each person should pay: ${final_amount}")


