# Write a Python Program capable of playing Rock, Paper, Scissor game with the user.

import random as rd

print("INSTRUCTIONS:")
print("r for rock")
print("p for paper")
print("s for scissor")

computer = rd.choice(['r', 'p', 's'])
user = input("Enter your choice: ").lower()
dict = {'r': "Rock", 'p': "Paper", 's': "Scissor"}

if (user == computer):
    print("You chose : ", dict[user])
    print("Computer chose : ", dict[computer])
    print("It's a Draw !!")
    print("Are you a Supercomputer ?!!!")
elif (user == 'r' and computer == 'p'):
    print("You chose : ", dict[user])
    print("Computer chose : ", dict[computer])
    print("Rock gets grabbed by Paper")
    print("You Lose !!")
elif (user == 'p' and computer == 'r'):
    print("You chose : ", dict[user])
    print("Computer chose : ", dict[computer])
    print("Paper catches Rock")
    print("You Won !!")
elif (user == 'r' and computer == 's'):
    print("You chose : ", dict[user])
    print("Computer chose : ", dict[computer])
    print("Rock crushes the scissor")
    print("You Won !!")
elif (user == 's' and computer == 'r'):
    print("You chose : ", dict[user])
    print("Computer chose : ", dict[computer])
    print("Scissor gets crushed by the Rock")
    print("You Lose !!")
elif (user == 'p' and computer == 's'):
    print("You chose : ", dict[user])
    print("Computer chose : ", dict[computer])
    print("Paper turned to pieces by the Scissor")
    print("You Lose !!")
elif (user == 's' and computer == 'p'):
    print("You chose : ", dict[user])
    print("Computer chose : ", dict[computer])
    print("Scissor cuts the Paper")
    print("You Won !!")
else:
    print("Something went wrong")
