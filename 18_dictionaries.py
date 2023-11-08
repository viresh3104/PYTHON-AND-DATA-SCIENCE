# dic are ordered collection of data types
# they can multiple values in sigle variable
# values are seprared by commnas and enclosed with in curly brackets{}

info = {  "name" : "viresh", "age" : 18 , "std" : 8   }
print(info["age"])
print(info["std"])
print(info["std"])

print(info.keys())       # name , age , std are keys

for key in info.keys():
    print (f"the key corresponds to {key} is", info[key])  