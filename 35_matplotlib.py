import pandas 
import matplotlib.pyplot as plt

data = pandas.read_csv("DA.csv")
plt.plot(data.emp_id , data.salary)
# plt.scatter(data.emp_id , data.salary)
# plt.bar(data.emp_id , data.salary)

plt.xlabel('Employee ID')
plt.ylabel('Salary')
plt.title('Salary vs Employee ID')
plt.show()