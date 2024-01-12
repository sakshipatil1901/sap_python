import math

def paint_calculator(height,width,cover):
    area=height*width
    number_of_cans=math.ceil(area/cover)
    print(f"You will need {number_of_cans} cans of paint.")

h=int(input("Enter the height of wall in meters:\n"))
w=int(input("Enter the width of wall in meters:\n"))
coverage=7
paint_calculator(width=w,height=h,cover=coverage)