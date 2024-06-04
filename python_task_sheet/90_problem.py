# Write a Python program to determine the grade of a student based on their marks using the following criteria:
# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# F: <60


def grade_system(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"
    
mark_input = float(input("Enter your marks:: "))
print("Your grade is:: ", grade_system(mark_input))
