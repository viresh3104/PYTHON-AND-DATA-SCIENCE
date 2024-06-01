# Write a Python program to convert a given number of seconds into hours, minutes, and seconds.
def coversion(input):
    hour = input // 3600
    min = (input % 3600) // 60
    seco = (input % 3600) % 60
    return hour, min, seco

input = int(input("Enter the number of seconds: "))
x = coversion(input)
print(x[0] ,"hr:", x[1] , "min:",x[2] ,"sec")