#WITHOUT ARGUMENTS AND WITHOUT RETURN VALUES
def sum():
    a=20
    b=30
    add=a+b
    print(add)
sum()

#WITH ARGUMENTS AND WITHOUT RETURN VALUES
def sum(a,b):
    c=a+b
    print(c)
sum(40,40)

#WITHOUT ARGUMENTS AND WITH RETURN VALUES
def sum():
    a=30
    b=20
    return a+b
print(sum())

#WITH ARGUMENTS AND WITH RETURN VALUES
def sum(a,b):
    c=a+b
    return c
add=sum(20,10)
print(add)

#RETURN STATEMENT
def sum(a,b):
    return a+b
print(sum(30,30))
