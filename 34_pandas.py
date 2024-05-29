# learning data analysis with panda
import pandas 

# Print the csv file
data = pandas.read_csv("DA.csv")
print("data::\n" ,data)


#  # Print only salary column or one coloum in a file
print("data.salary::\n",data.salary)



# find  max , min , sum , avg of salary using this functions 
print("maximun salary among all data::",data.salary.max())
print("minimum salary among all data::",data.salary.min())
print("total salary among all data::",data.salary.sum())
print("average salary among all data::",data.salary.mean())


# find specific value from coloum
print("finding data of employee 105 :: \n",data[data.emp_id == 105])

print("finding employee with max salary :: \n" ,data[data.salary == data.salary.max()])

print("Finding data of employee whose dept is Loan::\n", data[data.dept == "Loan"])


# print two coloums only by combining them , here we are combining first name and last name coloums foe 103 
print("#"*50)
emp_idd = data[data.emp_id == 103]
print("combining two coloums name and last name  :: ",emp_idd.fname.values[0], emp_idd.Iname.values[0])


# chaning data in any perticular coloum , here we're changing salary of sham to 10k
print("#"*50)
data.loc[data.emp_id == 102 , "salary"] =999999
print(data)


# deleting data entry of any perticular index number 
# frist we will learn how to find index number 
print("#"*50)
index_number = data.index[data.emp_id == 107][0]
print("finding index number :: ",index_number)
# now we will learn how to delete all the data from that index
print("#"*50)
data = data.drop(6)                            #here 6 is a index number
print(data)          #here data of leena is wiped out whic is at 6th index
# this will drop whole row for that index , now we'll learn how to delete a sngle coloum , here we are deleting desig coloum
print("#"*50)
data = data.drop(" desig" , axis=1)
print(data)           #this will remove desig column from our dataset



# sort the data in ascending order
print("#"*50)
data = data.sort_values(by="salary")      #by is used for using salary coloum data is going to sort
print("ascending order :: \n",data)
# sorting in descending order
print("#"*50)
data = data.sort_values(by="salary",ascending=False)     #you can also use desc=True instead of ascending=False
print("decending order :: \n",data)





# if we want to perfrom any action on a coloum 
# here we are performing action on salary coloum , and we are making new coloum to store that 
print("#"*50)
data['bonus'] = data.salary*0.1
print(data)




# now we will add one more coloum as total salary by adding salary + bonus
print("#"*50)
data['total_salary'] = data.salary + data.bonus
print(data)



# now to store all this modification to a file 
data.to_csv("DA_MODIFIED.csv")