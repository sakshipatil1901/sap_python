max = int(input("Enter a positive integer: "))
square_sum = 0

for number in range(2, max + 1, 2):
    square_sum += number

print("Sum of squares up to", max, "is:", square_sum)