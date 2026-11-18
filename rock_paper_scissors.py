#Charles Ajjan
#cmp131
#week10
#lab1
#Rock Paper Scissors
#date started on 11-10-26
import random

def get_computer_choice():
    choices = random.randint(1,3)
    if choices == 1:
        return "Rock"
    elif choices == 2:
        return "Paper"
    else: 
        return "Scissors"

def get_user_choice():
    get_user_choice = input("Enter your choice (1 for Rock, 2 for Paper, or 3 for Scissors): ")
    if get_user_choice == 1:
            return "Rock"
    elif get_user_choice == 2:
            return "Paper"
    else: 
            return "Scissors" 

def determine_winner(get_user_choice, get_computer_choice):
    if get_user_choice == get_computer_choice:
        return "tie"
    
    elif (
        (get_user_choice == "Rock" and get_computer_choice == "Scissors") or
        (get_user_choice == "Paper" and get_computer_choice == "Rock") or
        (get_user_choice == "Scissors" and get_computer_choice == "Paper")
    ):
        return "get_user_choice"
    
    return "get_computer_choice"

def display_result(winner, get_user_choice, get_computer_choice):
    if winner == "tie":
        print(f"Both chose {get_user_choice}. It's a tie!\n")
    elif winner == get_user_choice:
        print(f"You win! {get_user_choice} beats {get_computer_choice}.")
    else: 
        print(f"Computer wins! {get_computer_choice} beats {get_user_choice}.")

def main():
    print("Welcome to Rock, Paper, Scissors!")
    
   
    computer_choice = get_computer_choice()
    user_choice = get_user_choice()
    winner = determine_winner(user_choice, computer_choice)
    display_result(winner, user_choice, computer_choice)
main()
