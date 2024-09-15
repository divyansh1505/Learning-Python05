import random

"""
-1 Paper
1 Scissor 
0 Rock """
computer = random.choice([-1, 0, 1])

gameDict = {"s": 1, "p": -1, "r": 0}
reverseDict = {1 : "Scissor", -1 : "Paper", 0 : "Rock"}
youri = input("Enter your choice : ")
choice = gameDict[youri]      #Key se value ka variable bana lia 

print(f"You choose {reverseDict[gameDict[youri]]}")
print(f"Computer choose {reverseDict[computer]}")

if (choice == 1 and computer == -1):
    print("You win")
elif (choice == -1 and computer == -1):
    print("Draw")
elif (choice == 0 and computer == -1):
    print("You loose")
elif (choice == 0 and computer == 1):
    print("You Win")
elif (choice == 0 and computer == 0):
    print("Draw")
elif (choice == 1 and computer == 1):
    print("Draw")
elif (choice == 1 and computer == 0):
    print("You loose")
elif (choice == -1 and computer == 0):
    print("You win")
elif (choice == -1 and computer == 1):
    print("You loose")
else:
    print("Thanks for playing")