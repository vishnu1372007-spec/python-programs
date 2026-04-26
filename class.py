class display:
    def __init__(self,name):
        self.name=name
d1=display("Hi")
print(d1)

class display:
    def __init__(self,name):
        self.name=name
    def __str__(self):
            return "student name is:"+self.name
d1=display("Silence")
print(d1)


class display:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return student name and age is{f}:,self.name,self.age
p=display("Vishnu",15)
print(p)
