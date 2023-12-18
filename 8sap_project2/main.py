print("Welcome to tip calculator.")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip will you pay? 5, 7 or 14? "))
person = int(input("How many persons will split the bill?"))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / person
final_amount = round(bill_per_person, 2)
final_amount = "{:.2f}". format(bill_per_person)
print(f"Each person should pay: ${final_amount}")
