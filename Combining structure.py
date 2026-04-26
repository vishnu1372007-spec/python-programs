#COMBINING STRUCTURE:
class Employee:
    def __init__(self,name):
        self.name=name
    def works(self):
        print("Employees do the work")
class Manager(Employee):
    def work(self):
        print(self.name,"The Manager manages the team")
class Tester(Employee):
    def work(self):
        print(self.name,"The Tester tests the code")
def Employee_details(emp):
        emp.work()
m=Manager("Girls")
t=Tester("Boys")
Employee_details(m)
Employee_details(t)
