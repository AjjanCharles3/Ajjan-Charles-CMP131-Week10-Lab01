#Charles Ajjan
#cmp131
#week10
#lab1
#Rock Paper Scissors
#date started on 11-10-26
import random

def get_computer_choice():
    choices = ["Rock", "Paper", "Scissors"]
    return random.choice(choices)

def get_user_choice():
    valid_choices = ["Rock", "Paper", "Scissors"]
    while True:
        user_input = input("Enter your choice (Rock, Paper, or Scissors): ")
        if user_input in valid_choices:
            return user_input
        print("Invalid choice. Please type Rock, Paper, or Scissors.\n")

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    
    if (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Paper" and computer_choice == "Rock") or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        return "user"
    
    return "computer"

def display_result(winner, user_choice, computer_choice):
    if winner == "tie":
        print(f"Both chose {user_choice}. It's a tie! Replaying the round...\n")
    elif winner == "user":
        print(f"You win! {user_choice} beats {computer_choice}.")
    else:
        print(f"Computer wins! {computer_choice} beats {user_choice}.")

def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    
    while True:
        computer_choice = get_computer_choice()
        user_choice = get_user_choice()
        print(f"\nComputer chose: {computer_choice}")
        winner = determine_winner(user_choice, computer_choice)
        display_result(winner, user_choice, computer_choice)
        
        if winner != "tie":
            break

if __name__ == "__main__":
    play_game()
