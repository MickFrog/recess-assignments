# Ssenono Jordan Michael
# 21/U/1013
# 2100701013

# celcius_temp = float(input("Provide a celcius temperature to be converted to Fahrenheit: "))

# fht_temp = (celcius_temp / (9 / 5)) + 32

# print(fht_temp)

class Employee:
    def __init__(self, name, job, salary):
        self.__name = name
        self.__job = job
        self.__salary = salary + 150000
    
    def getDetails(self):
        print("Name:", self.__name)
        print("Job:", self.__job)
        print("Salary:", self.__salary)

myEmployee = Employee("Kalooli Lwanga", "Software Engineer", 850000)

myEmployee.getDetails()