import random
computer_score=0
user_score=0
options=["rock","paper","sissior"]


while True:
    print("Do u want to play")
    user_input=input("choose rock/paper/sissior or Q to quit\n").lower()
    if user_input == "q":
        break
    elif user_input not in options:
        continue
    
    random_numbers=random.randint(0,2)
    computer_input=options[random_numbers]
    print("computer picked",computer_input,"\n")
    
    if user_input == "rock" and computer_input == "sissior":
        print("You won!\n")
        user_score+=1

    elif user_input == "paper" and computer_input == "rock":
        print("You won!\n")
        user_score+=1

    elif user_input == "sissior" and computer_input == "paper":
        print("You won!\n")
        user_score+=1

    elif user_input == "sissior" and computer_input == "sissior":
        print("Its a Tie\n")
    
    elif user_input == "paper" and computer_input == "paper":
        print("Its a Tie")
        
    elif user_input == "rock" and computer_input == "rock":
        print("Its a Tie\n")

    else:
        print("You lost\n")
        computer_score += 1

print("computer_score" ,computer_score,"\n")
print("user_score" ,user_score,"\n")    
