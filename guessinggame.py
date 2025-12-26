import random

number = random.randint(1,100)
userTries = 0
correctGuess = 0

print(number)

print("Guess a number between 1 and 100")
while correctGuess == 0:    
    guessedNumber = int(input())
    if guessedNumber == number:
        print("Congratulations! You guessed it correctly. It took you", userTries + 1, "tries.")
        break
    else:
        if guessedNumber < number:
            print("Guess Higher!")
            userTries = userTries + 1
        else:
            print("Guess Lower!")
            userTries = userTries + 1