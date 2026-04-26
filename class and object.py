class dog:
    attr1="puppy"
    attr2="snoopy"
    def display(self):
        print("This is",self.attr1)
        print("This is",self.attr2)
tomy=dog()
print(tomy.attr1)
tomy.display()
        
class person:
    name="Vishnu"
    age="18"
    def display(self):
        print("My name is:",self.name)
        print("age is:",self.age)
p=person()
print(p.name)
p.display()
