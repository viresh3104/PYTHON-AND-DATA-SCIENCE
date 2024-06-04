# Write a Python program to calculate the BMI (Body Mass Index)
# given weight in kilograms and height in meters.


def bmi(weight:float,height:float) -> float:
    bmi_cal = weight / (height**2)
    return bmi_cal

input_weight = float(input("Enter the weight:"))
input_height = float(input("Enter the height in cm :")) / 100
print("BMI is:",bmi(input_weight,input_height))


