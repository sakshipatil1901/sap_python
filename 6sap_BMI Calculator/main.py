weight = int(input("Enter your weight in Kg: "))
height = float(input("Enter your height in meters: "))

BMI = weight / (height ** 2)

bmi_result = int(BMI)

print(f"Your BMI is: {bmi_result}")