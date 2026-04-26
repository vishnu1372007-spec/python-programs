try:
    f=open("example13","r")
    f.read("friday is python lab")
    f.close()
except FileNotFoundError:
    print("File not found")
finally:
    print("Code runs successfully")
    
