try:
     marks=25
     result=25/0
     print(result)
except ZeroDivisionError:
    print("A number cannot be divide by zero")

try:
 list=[1,3,5,7]
 print(list[7])
except IndexError:
    print("Element not found")
