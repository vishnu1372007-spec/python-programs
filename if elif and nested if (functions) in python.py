#if-elif

def userchoice(userchoice):
    if(userchoice==1):
       print("admin")
    elif(userchoice==2):
       print("guest")
    elif(userchoice==3):
       print("worker")
    else:
       print("enter valid choice")
userchoice(2)


#nested if
a=int(input("enter a number"))
b=int(input("enter b number"))
if(a>b):
    print("a is big")
    if(a==b):
        print("a and b are equal")
    else:
        print("a and b are not equal")
else:
    print("b is big")

    
