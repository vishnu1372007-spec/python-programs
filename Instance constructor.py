class numdisplay:
    def __init__(self):
        self.x=100
    def display(self):
        y=30
        print("Instance variable is:",self.x)
        print("Normal variable is:",y)
n1=numdisplay()
n1.display()
print("Outside instance variable is:",n1.x)
print(y)
