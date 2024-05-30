# Write a Python program to find the volume of a cylinder given its
# radius and height. Use the formula V = πr²h (use 3.14159 for π).

print("this program is used to find the volume of cylinder, enter its height and radius::")


input_radius = int(input("Enter the radius::"))
input_height = int(input("Enter the height ::"))

def volume_of_cylinder(radius , height):
    volume = 3.14 * (radius**2) * (height)
    return volume

x = volume_of_cylinder(input_radius , input_height)
print("volume of given cylinder is :: ",x)