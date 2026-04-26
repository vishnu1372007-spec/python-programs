class ValueTooSmallError(Exception):
    """Raised when the input value is too small"""
    pass
class ValueTooLargeError(Exception):
    """Raised when the input value is too large"""
    pass
age = 18
while True:
    try:
        i_num=int(input("Enter age:"))
        if i_num < number:
            raise ValueTooSmallError
        elif i_num > number:
            raise ValueTooLargeError
        break
    except ValueTooSmallError:
        print("Age is too young,age is not valid!")
        print()
    except ValueTooLargeError:
        print("Age is too old,age is not valid!")
        print()
print("Congratulations! You valid for voting.")
            
