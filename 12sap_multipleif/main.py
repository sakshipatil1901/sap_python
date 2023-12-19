height = int(input("What is your height? "))
bill = 0
if height >= 3:
    print("can ride.")
    age=int(input("What is your age? "))
    if age < 12:
        bill = 150
        print("Ticket price is 150 Rs.")
    elif age <= 18:
        bill = 250
        print("Ticket price is 250 Rs.")
    else:
        bill = 500
        print("Ticket price is 500 Rs.")
    take_photo = input("Do you want to take photo(Y/N)? ")
    if take_photo == 'y' or take_photo == 'Y':
        bill = bill + 50
    print(f"Your total bill is {bill}")

else:
    print("can't ride..")
print("Thank you..Enjoy the ride.")