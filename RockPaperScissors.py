import random               # using it to generate computer choices

while True:
    #user input
    user_action = input("Enter a choice (rock, paper, scissors): ") 
    
    # computer chooses 
    possible_actions = ["rock", "paper", "scissors"]
    
    #computer action 
    computer_action = random.choice(possible_actions)   #computer selects a random  action using random.choice 

    # print the choices that the user and the computer made:
    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

     #Determine a Winner
    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!") #in the event that its a tie and user & computer choose paper 
    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_action == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")
