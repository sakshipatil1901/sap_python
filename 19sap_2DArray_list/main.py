Two_D_Array = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'i']
]

print("Two_D_Array: ")
for row in Two_D_Array:
    print(row)

position = input("Enter the position: ")


row_number = int(position[0])
column_number = int(position[1])


Two_D_Array[row_number - 1][column_number - 1] = '#'

print("Updated Array:")
for row in Two_D_Array:
    print(row)