try:
  a='ab'
  print(int(a))
except ValueError:
    print("value not found")
finally:
    print("Code runs successfully")

try:
  att=23
  print(Att)
except NameError:
    print("Name not found")
finally:
    print("Code runs successfully")

try:
   f=open("Studentregistration.txt","r")
   c=f.read()
   f.close
except FileNotFoundError:
         print("File not found")
finally:
    print("Code runs successfully")

try:        
  a='23'
  b=32
  print(a+b)
except TypeError:
    print("Type error not found")
finally:
     print("Code runs successfully")

try:
  a=23
  b=0
  print(a/b)
except ZeroDivisionError:
    print("number is not divided by zero")
finally:
    print("Code runs successfully")

try:
    list=[1,2,3,4,5]
    print(list[7])
except IndexError:
    print("Index is not found")
finally:
    print("Code runs successfully")   
