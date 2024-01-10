def print_2d_array(arr):
    print("Two_D_Array:")
    for row in arr:
        print(row)


rows = 3
columns = 3
Two_D_Array = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]


print_2d_array(Two_D_Array)


for i in range(rows * columns):
    if i % 2 == 0:
        user = "User 1"
        symbol = 'X'
    else:
        user = "User 2"
        symbol = 'O'


    valid_position = False
    while not valid_position:
        position = input(f"{user} - Enter the position: ")

        if ' ' not in position:
            print("Invalid input. Please enter two integers separated by a space.")
            continue

        row, col = map(int, position.split())

        if 1 <= row <= rows and 1 <= col <= columns and Two_D_Array[row - 1][col - 1] == ' ':
            valid_position = True
        else:
            print("Invalid input. Please enter a valid position.")


    if Two_D_Array[row - 1][col - 1] in ['X', 'O']:
        print(f"Position already occupied. {user}, please choose a different position.")
    else:
        Two_D_Array[row - 1][col - 1] = symbol
        print_2d_array(Two_D_Array)