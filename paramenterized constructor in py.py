class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("Name is:",self.name)
        print("Age is:",self.age)
p1=person("Madhu",24)
p1.display()
    
class addition:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def display(self):
        print("Result is:",self.a+self.b)
c=addition(20,30)
c.display()
