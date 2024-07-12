import random

choices = ["Rock","Paper","Scissor"]
userScore = 0
computerScore = 0

def gamePlay(userScore,computerScore):
    x= random.sample(choices,1)
    computerAction = "".join(x)

    choice = int(input("Press 1 for Rock, 2 for Paper or 3 for Scissor: "))

    if choice == 1:
        userAction = "Rock"
    elif choice == 2:
        userAction = "Paper"
    elif choice == 3:
        userAction = "Scissor"
    else:
        print("Invalid action!! Exiting game...")
        return

    print("User:",userAction)
    print("Computer:",computerAction)


    if ((userAction == "Rock" and computerAction == "Scissor") or (userAction == "Paper" and computerAction == "Rock") or(userAction == "Scissor" and computerAction == "Paper")):
        userScore+=1
        computerScore-=1
        print("User Wins!")

    elif ((userAction == "Paper" and computerAction == "Scissor") or (userAction == "Scissor" and computerAction == "Rock") or (userAction == "Rock" and computerAction == "Paper")):
        userScore-=1
        computerScore+=1
        print("Computer Wins!")

    elif(userAction==computerAction):
        userScore+=0
        computerScore+=0
        print("It's a Tie!")

    print("User Score:",userScore)
    print("Computer Score:",computerScore)
    n = int(input("Want to Play another round? Press 1, Else press any other numeric key: "))
    print()
    if n==1:
        gamePlay(userScore,computerScore)
    else: 
        if userScore>computerScore:
            print("Overall winner is User!")
        elif userScore<computerScore:
            print("Overall winner is Computer!")
        else:
            print("Overall Tie")
        return

gamePlay(userScore,computerScore)
