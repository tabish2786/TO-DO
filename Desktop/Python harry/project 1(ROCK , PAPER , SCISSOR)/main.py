import random

'''
1 for rock
-1 for paper
0 for scissor
'''

computer = random.choice([-1, 0, 1])

youstr = input("Enter r (rock), p (paper), s (scissor): ").lower()

youDict = {"r": 1, "p": -1, "s": 0}
reverseDict = {1: "Rock", -1: "Paper", 0: "Scissor"}

if youstr not in youDict:
    print("Invalid input!")
    exit()

you = youDict[youstr]

print(f"You chose {reverseDict[you]}")
print(f"Computer choosed {reverseDict[computer]}")

if computer == you:
    print("It's a draw")

elif you == 1 and computer == 0:      

    print("You win!")

elif you == 0 and computer == -1:     
    print("You win!")

elif you == -1 and computer == 1:     
    print("You win!")

else:
    print("You lose!")
