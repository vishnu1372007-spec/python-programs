#SINGLE INHERITANCE:
class A:
    def one(self):
        print("This is base class")
class B(A):
    def two(self):
        print("This is derived class")
obj=B()
obj.one()
obj.two()

#MULTI-LEVEL INHERITANCE:
class A:
    def one(self):
        print("This is base class")
class B(A):
    def two(self):
        print("This is derived class")
class C(B):
    def three(self):
        print("This is another class")
obj=C()
obj.one()
obj.two()
obj.three()

class Father:
    def Father(self):
        print("This is base class")
class Mother:
    def Mother(self):
        print("This is derived class")
class Child(Father,Mother):
    def Child(self):
        print("This is another class")
obj=Child()
obj.Father()
obj.Mother()
obj.Child()

        
