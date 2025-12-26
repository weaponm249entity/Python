import random
import statistics

a = int(random.randrange(0,1000))
b = int(random.randrange(0,1000))
c = int(random.randrange(0,1000))
d = int(random.randrange(0,1000))
e = int(random.randrange(0,1000))
f = int(random.randrange(0,1000))
g = int(random.randrange(0,1000))
h = int(random.randrange(0,1000))

numbers = [a,b,c,d,e,f,g,h]
sortedNumbers = sorted(numbers)
numTotal = numbers[0] + numbers[1] + numbers[2] + numbers[3] + numbers[4] + numbers[5] + numbers[6] + numbers[7]
numAverage = numTotal/len(numbers)
numMedian = (sortedNumbers[len(numbers)//2] + sortedNumbers[len(numbers)//2 + 1]) // 2

sum

print("-----------------------------------------") 
print("Sorted Numbers")
print(sortedNumbers)
print("-----------------------------------------")
print("Minimum of Numbers")
print(sortedNumbers[0])
print("-----------------------------------------")
print("Maximum of Numbers")
print(sortedNumbers[7])
print("-----------------------------------------")
print("Numbers Total")
print(numTotal)
print("-----------------------------------------")
print("Average of Numbers")
print(numAverage)
print("-----------------------------------------")
print("Numbers Median")
print(numMedian)


