def factorial(num):
        factOut = 1
        while True:
            factOut = factOut * num
            num = num - 1
            if num == 0:
                break
        return factOut

print(factorial(factorial(30)))