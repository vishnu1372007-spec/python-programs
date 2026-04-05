a=int(input("enter a value"))
b=int(input("enter b value"))
n=int(input("enter n value:"))
for i in range(n):
    print(a,end=" ")
    c=a+b
    a=b
    b=c
print()
