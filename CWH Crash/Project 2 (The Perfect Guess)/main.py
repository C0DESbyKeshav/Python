# We are going to write a program that generates a random number and asks the user to guess it.
# If the player's guess is higher than the actual number, the program displays "lower number please".
# Similarly, if the user's guess is too low, the program prints "higher number please".
# When the user guesses the correct number, the program displays the number of guesses the player used to arrive at the number.
# Hint: Use the random module.

import random

# Generate a random number between 1 and 100
randomNumber = random.randint(1, 100)

num = 0
guesses = 0
while(num != randomNumber):
    num = int(input("Guess a number between 1 and 100: "))
    if (num < randomNumber):
        print("Higher number please.\n")
    elif (num > randomNumber):
        print("Lower number please.\n")
    guesses += 1
    
print(f"Congratulations! You guessed the number {randomNumber} in {guesses} tries.")
