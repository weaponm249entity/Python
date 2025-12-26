sumOfNumbers = 0
sumOfOdd = 0
sumOfEven = 0
maxNum = 92
j=1

for i in range(1,maxNum+1):
    sumOfNumbers = sumOfNumbers + i
print(sumOfNumbers)
print("----------------------")
if maxNum % 2 == 0:
    while j < maxNum+1:
        sumOfOdd = sumOfOdd + j
        sumOfEven = sumOfEven + j + 1
        j = j + 2
else:
    while j < maxNum-1:
        sumOfOdd = sumOfOdd + j
        sumOfEven = sumOfEven + j + 1
        j = j + 2
    sumOfOdd = sumOfOdd + maxNum    
print(sumOfOdd)
print(sumOfEven)

