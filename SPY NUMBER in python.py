#SPY NUMBER

n=int(input("Enter a number:"))
sum digits=0
product digits=1
temp=n
while temp>0:
    digit=temp%10
    sum digits+=digit
    product digits*=digit
    temp=temp//10
if sum digits==product digits:
    print("Spy Number")
else:
    print("Not a Spy Numbers")
