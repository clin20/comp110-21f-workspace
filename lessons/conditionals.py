"""example of conditionial (if-else) statements"""

SECRET: int = 3

print("I'm thinking of a nuumber between 1-5, what is it?")
guess: int = int(input("What is your guess? "))

if guess == SECRET:
    print("You guessed corectly!!!")
else:
    print("You guessed incorrectly. :(")
    
    if guess > SECRET:
        print("Too high!")
    else:
        print("Too low!")
    

print("Game over.")