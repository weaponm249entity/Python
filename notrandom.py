import random

randNum = random.randrange(1,100)

rmngTries = 6

# print (randNum) # delete or comment after debugging

while 1 <= rmngTries:
    print("Enter a random number between 1-100...")
    entNum = int(input())
    if entNum == randNum :
        break
    elif entNum > randNum :
        rmngTries = rmngTries - 1
        print("Guess Lower.")
        print("")
    else :
        rmngTries = rmngTries - 1
        print("Guess Higher.")
        print("")
if rmngTries == 0 :
    print('You Lost! It was', randNum)
else :
    print("You Win!")