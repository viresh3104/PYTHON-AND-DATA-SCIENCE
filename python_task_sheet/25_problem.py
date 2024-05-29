# Create a program that checks if two sets have any elements in common.


def is_common(set_a , set_b):
    if set_a.intersection(set_b):
        return True
    
set_a = {"computer science","IT","AI","DS"}
set_b = {"IT","ELECTRICAL","MEC","AI"}

print(is_common(set_a,set_b))