import os
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
operations_dict={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}

def calculator():
    num1 = float(input("Enter first number: "))
    for symbol in operations_dict:
        print(symbol)

    continue_flag=True
    while continue_flag:
        op_symbol = input("Pick an operation: ")
        num2 = float(input("Enter second number: "))
        calculator_function=operations_dict[op_symbol]
        output=calculator_function(num1, num2)
        print(f"{num1} {op_symbol} {num2} = {output}")


        To_continue = input(f"Enter 'y' to continue calculation with {output} or 'n' to start new calculation 'x' to exit").lower()
        if To_continue=='y':
            num1 = output
        elif To_continue=='n':
            continue_flag=False
            os.system('cls')
            calculator()
        else:
            continue_flag=False
            print("Bye")
calculator()
