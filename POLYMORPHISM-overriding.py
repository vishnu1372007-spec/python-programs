#POLYMORPHISM

#2.METHOD OVERRIDING:
class Mother:
    def parent(self):
        print("This is base class")
class Child(Mother):
    def parent(self):
        super().parent()
        print("This is child class")
ch=Child()
ch.parent()

class Animal:
     def Sound(self):
        print("Cat do the sound Meow")
class Dog(Animal):
     def Sound(self):
        super().Sound()
        print("Dog do the sound Bow")
A=Dog()
A.Sound()

