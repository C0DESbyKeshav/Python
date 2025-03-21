# The game() function in a program lets a player play a game and returns the score as an integer. You need to read a file "02_HiScore.txt" which is either blank or contains the previous Hi-score. You need to write a program to update the Hi-score whenever game() breaks the Hi-score.
import random


def game():
   choicesAvail = {1: "Rock", 2: "Paper", 3: "Scissor"};
   reverseChoicesAvail = {"Rock":1, "Paper":2, "Scissor":3};
   player = int(input("CONTROLS:\n1 for Rock\n2 for Paper\n3 for Scissor\n"));
   computer = random.choice(choicesAvail);
   # print(player, reverseChoicesAvail[computer]);  # Numeric values
   # print(choicesAvail[player], computer);  # String values
   
   ''' LENGTHY METHOD:
   if (player == reverseChoicesAvail[computer]):
       print("You chose : ", choicesAvail[player])
       print("Computer chose : ", computer)
       print("It's a Draw !!")
       print("Are you a Supercomputer ?!!!")
   elif (player == 1 and reverseChoicesAvail[computer] == 2):      # 1-2 = -1
       print("You chose : ", choicesAvail[player])
       print("Computer chose : ", computer)
       print("Rock gets grabbed by Paper")
       print("You Lose !!")
   elif (player == 1 and reverseChoicesAvail[computer] == 3):      # 1-3 = -2
       print("You chose : ", choicesAvail[player])
       print("Computer chose : ", computer)
       print("Rock crushes the scissor")
       print("You Won !!")
   elif (player == 2 and reverseChoicesAvail[computer] == 1):      # 2-1 = 1
       print("You chose : ", choicesAvail[player])
       print("Computer chose : ", computer)
       print("Paper catches Rock")
       print("You Won !!")
   elif (player == 2 and reverseChoicesAvail[computer] == 3):      # 2-3 = -1
       print("You chose : ", choicesAvail[player])
       print("Computer chose : ", computer)
       print("Paper turned to pieces by the Scissor")
       print("You Lose !!")
   elif (player == 3 and reverseChoicesAvail[computer] == 2):      # 3-2 = 1
       print("You chose : ", choicesAvail[player])
       print("Computer chose : ", computer)
       print("Scissor cuts the Paper")
       print("You Won !!")
   elif (player == 3 and reverseChoicesAvail[computer] == 1):      # 3-1 = 2
       print("You chose : ", choicesAvail[player])
       print("Computer chose : ", computer)
       print("Scissor gets crushed by the Rock")
       print("You Lose !!")
   else:
       print("Something went wrong")
   '''
   
   # SHORT METHOD: By observing the pattern from the lengthy method.
   score = 0
   if (player == reverseChoicesAvail[computer]):
       print("You chose : ", choicesAvail[player])
       print("Computer chose : ", computer)
       print("It's a Draw !!")
       score = 2
   elif(player - reverseChoicesAvail[computer] == 1 or player - reverseChoicesAvail[computer] == -2):
       print("You chose : ", choicesAvail[player])
       print("Computer chose : ", computer)
       print("You Won !!")
       score = 5
   elif(player - reverseChoicesAvail[computer] == -1 or player - reverseChoicesAvail[computer] == 2):
       print("You chose : ", choicesAvail[player])
       print("Computer chose : ", computer)
       print("You Lose !!")
       score = -1
   else:
       print("Something went wrong")
       
   with open("02_HiScore.txt") as f:
        hiscore = f.read()
        if (hiscore != ""):
            hiscore = int(hiscore)  # when we read from a file, it returns the contents of the file as a string so, to obtain it in a numberical value form, we first have to convert it into an integer
        else:
            hiscore = 0
    
   print("Your score is : ", score)
   print("Your high score is : ", hiscore)
   
   if (score > hiscore):
        # write this hiscore to the file
        with open("02_HiScore.txt", "w") as f:
            f.write(str(score))  # we can only write the into the file in the string format


game();
