
class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("My name is:",self.name)
        print("Age is:",self.age)
s1=student("Hello",15)
s1.display()


class car:
    def __init__(self,model,cost,color):
        self.model=model
        self.cost=cost
        self.color=color
    def display(self):
        print("model is:",self.model)
        print("cost is:",self.cost)
        print("color is:",self.color)
c=car("Rollsroyce",10000000,"Black")
c.display()
        
