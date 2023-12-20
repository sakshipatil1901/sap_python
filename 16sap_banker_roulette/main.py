import random

name = input("Enter everybody's name separated by comma: ")
names_list = name.split(",")
print(names_list)
length = len(names_list)
choice=random.randint(0, length-1)
option=random.choice(names_list)
print(f"{option} will pay the bill")

