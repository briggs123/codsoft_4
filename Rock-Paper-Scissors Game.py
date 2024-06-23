import random

def get_user_choice():
    while True:
        print("\nPlease choose:")
        print("1 - Rock")
        print("2 - Paper")
        print("3 - Scissors")
        user_input = input("Enter your choice (1, 2, or 3): ").strip()
        
        choices = {"1": "rock", "2": "paper", "3": "scissors"}
        if user_input in choices:
            return choices[user_input]
        else:
            print("Invalid choice. Please try again.")

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"

def display_result(user_choice, computer_choice, winner):
    print(f"\nYou chose: {user_choice.capitalize()}")
    print(f"Computer chose: {computer_choice.capitalize()}")
    if winner == "tie":
        print("It's a tie!")
    elif winner == "user":
        print("Congratulations! You win!")
    else:
        print("You lose. Better luck next time!")

def play_again():
    while True:
        again = input("\nDo you want to play another round? (yes/no): ").strip().lower()
        if again in ["yes", "no"]:
            return again == "yes"
        else:
            print("Invalid input. Please type 'yes' or 'no'.")

def play_game():
    user_score = 0
    computer_score = 0
    
    print("Welcome to the Rock-Paper-Scissors game!")
    
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        winner = determine_winner(user_choice, computer_choice)
        display_result(user_choice, computer_choice, winner)
        
        if winner == "user":
            user_score += 1
        elif winner == "computer":
            computer_score += 1
        
        print(f"\nCurrent Score: You {user_score} - {computer_score} Computer")
        
        if not play_again():
            break

    print("\nThanks for playing! Final score:")
    print(f"You: {user_score} - {computer_score} Computer")

play_game()
