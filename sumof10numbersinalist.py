numbers = [1,2,3,4,5,6,7,8,9,10]
sumOfNumbers = 0
for i in range (len(numbers)-1):
    for j in range(i+1,len(numbers)):
        sumOfNumbers = numbers[i] + numbers[j] + sumOfNumbers
print(sumOfNumbers)