#MULTIPLE INHERITANCE:
class Mother:
    def Parent(self):
        print("This is Mother class")
class Father:
    def Parent1(self):
        print("This is Father class")
class Child(Mother,Father):
    def parchild(self):
        print("This is from Mother and Father class")
ch=Child()
ch.parchild()      #THIS IS FROM MOTHER AND FATHER 


#HYBRID INHERITANCE:
class Animal:
    def sound(self):
        print("Animals make sounds")
class mammal(Animal):
    def make_sound(self):
        print("Mammals make sound")
class Bird:
    def make_sound(self):
        print("Birds do th sounds")
class Bat(mammal,Bird):
    pass
obj=Bat()
obj.make_sound()
