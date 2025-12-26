import random

numbers = []

while len(numbers)<9:
        newNum = random.randint(0,100)
        if newNum not in numbers:
            numbers.append(newNum)

sumOfNumbers = 0
for i in numbers:
      sumOfNumbers = sumOfNumbers + i
maximumNum = numbers[0]
minimumNum = numbers[0]
for i in numbers:
    if i > maximumNum:
        maximumNum = i
    if i < minimumNum:
        minimumNum = i
print(maximumNum)
print(minimumNum)
for i in range(len((numbers))-1):
    for j in range(i+1,len((numbers))):
        if numbers[i] > numbers[j]:
             temp = numbers[i]
             numbers[i] = numbers[j]
             numbers[j] = temp
print(numbers)
numOfIndexes = len(numbers)
if numOfIndexes % 2 == 0 :
    median = 0
    print("Number of Indexes is even")
    medianA = (int(numOfIndexes/2)) - 1
    medianB = medianA + 1
    median = (numbers[medianA] + numbers[medianB]) / 2
    print(median)
else:
    print("Number of Indexes is odd")
    median = round((numOfIndexes)/2)
    print(numbers[median])