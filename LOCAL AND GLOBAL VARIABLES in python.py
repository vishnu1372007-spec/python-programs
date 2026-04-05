#VARIABLES

1.#LOCAL VARIABLES
def display():
    a=10
    print("inside value is:10",a)
display()

2.#GLOBAL VARIABLES
x=10
def display():
    print("inside fun:",x)
display()
print("outside fun:",x)

x=100
def display():
    x=10
    print("The value for inside:",x)
display()
print("The value for outside:",x)


#CHANGE GLOBAL VARIABLE VALUE
y=20
def change():
    global y
    y=40
change()
print(y)

