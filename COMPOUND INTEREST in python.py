#COMPOUND INTEREST

p=float(input("Enter Principal amount:"))
r=float(input("Enter Rate of interest:"))
t=float(input("Enter Time(in years):"))
amount=p*(1+r/100)**t
ci=amount-p
print("Total Amount=",amount)
print("Compound interest=",ci)
