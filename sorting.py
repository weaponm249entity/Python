import random

numCount = 25
LOLimit = 0
HILimit = 1000
numbers = []
tempNum = 0

while(len(numbers) != numCount):
    newNum = random.randint(LOLimit,HILimit)
    if newNum not in numbers:
        numbers.append(newNum)

print(numbers)
print("---------------------")

for i in range(len(numbers)-1):
    for j in range(i+1,len(numbers)):
        if numbers[i] < numbers[j]:
            tempNum = numbers[i]
            numbers[i] = numbers[j]
            numbers[j] = tempNum
print(numbers)
