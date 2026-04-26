try:
   f=open("Studentregistration.txt","r")
   c=f.read()
   f.close
except FileNotFoundError:
         print("File not found")
finally:
    print("Code runs successfully")
         
