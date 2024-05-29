# Given two sets, find the union, intersection, and difference between them

set_a = {"a" , "b" , "c" , "d" ,"e" , "f"}
set_b = {"g" , "h" , "i" ,"j" ,"k" , "e" , "d"}


temp_str = set_a.update(set_b)


union_str = set_a.union(set_b)

intersection_str = set_a.intersection(set_b)

different_str = set_a ^ set_b


print("intersection of two sets ::",intersection_str)
print("union of two sets ::",union_str)
print("differnet elements from two sets ::" , different_str)
