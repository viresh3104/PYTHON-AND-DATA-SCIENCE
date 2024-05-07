

class students:
    college = "G.H Raisoni, pune"     # this is applied to all objects (used in speciifc cases)

    def __init__(self, name, div, year, dep):
        self.name = name
        self.division = div
        self.year = year
        self.department = dep

    # everytime it is not possible to call this object one by one so we will make one class to call all objects once

    def stu_info(self):
        print(f"Name of Student is {self.name}")
        print(f"Division of {self.name} is {self.division}")
        print(f"{self.name} is in {self.year}")
        print(f"Department of {self.name} is {self.department}")

    # now if there is need to change any detail related to object then we will need to define a fun

    def change_year(self,new_year):
        self.year = new_year
        print(f"{self.name} is now in {new_year}")


stu_1 = students("viresh" , "C" , "second year" , "CSE_AI")
stu_2 = students("shiv" , "C" , "second year" , "CSE_AI")

print(stu_1.department)
print(stu_1.division)
print(stu_1.name)
print(stu_2.college)    # .college is globally distributed to all classes 
# Output : CSE_AI

stu_1.stu_info()
stu_2.stu_info()
# used to view all info i.e obj at once

stu_1.change_year("third year")
stu_1.stu_info()
# used to change the year for specific student


