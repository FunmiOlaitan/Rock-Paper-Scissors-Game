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