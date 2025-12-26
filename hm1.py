import os

def factorial(n):
        if n <= 1:
            return 1
        return n * factorial(n-1)
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
def sumlist(L):
    if len(L) == 0:
        return 0
    return L[0] + sumlist(L[1:])

myList = [1,2,3,4,5,6,7,8,9,10,11,12]
os.system("clear")
print(sumlist(myList))