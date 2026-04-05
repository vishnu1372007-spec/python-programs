#DEFAULT
def sum(x=10,y=30,z=20):
    add=x+y+z
    print(add)
sum(x=10,y=30,z=20)
sum(x=10)

#KEYWORD ARGUMENTS
def sum(x,y=30,z=40):
    addition=x+y+z
    print(addition)
sum(10,50,100)
sum(190)

#VARIABLE-LENGTH ARGUMENTS
def display(*no):
    print(no)
display(10,20,40)
