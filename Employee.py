#Python Program to demonstrate class
class Employee:

    empcount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary= salary
        Employee.empcount=+1

    def displayCount(self):
        print ("Total Employee Count: " % Employee.empcount)

    def displayEmployeeDetails(self):
        print ("Name: ",self.name, self.salary)


"This would create first object of Employee class"
employee1 = Employee("Joel", 7000)
"This would create second object of Employee class"
employee2 = Employee("Roberts", 9000)   
employee3 = Employee("Roberts3", 9000)        

employee1.displayEmployeeDetails()
employee2.displayEmployeeDetails()
employee3.displayEmployeeDetails()
print ("Total Employee %d" % Employee.empcount)
