#RECURSION

#Factorial
def fact(n):
    if  n==1:
        return 1
    else:
        return n*fact(n-1)
print(fact(5))

#Fibonacci
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

for i in range(10):
    print(fibonacci(i), end=" ")
