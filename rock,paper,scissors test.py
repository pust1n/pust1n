from random import randint


t = ["Rock", "Paper", "Scissors"]

computer = t[randint(0,2)]

player = False

while player == False:
    player = input("Rock, Paper, Scissors?")
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!")
        else:
            print("You win!")
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!")
        else:
            print("You win!")
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...")
        else:
            print("You win!")
    else:
        print("That's not a valid play. Check spelling!")
    
    player = False
    computer = t[randint(0,2)]
