import random

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    wins = 0
    losses = 0
    ties = 0
import random

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    wins = 0
    losses = 0
    ties = 0

while True:
    print("\nEnter your choice (rock, paper, or scissors). Type 'quit' to end the game.")
    user_choice = input().lower()
    
    if user_choice == 'quit':
        break
        
    if user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice, please choose rock, paper, or scissors.")
        continue
        
    computer_choice = get_computer_choice()
    print(f"Computer chose: {computer_choice}")
        
    result = determine_winner(user_choice, computer_choice)
    print(result)
        
    if result == "You win!":
        wins += 1
    elif result == "Computer wins!":
        losses += 1
    else:
        ties += 1
        
    print(f"Score: Wins: {wins} | Losses: {losses} | Ties: {ties}")
    
print("\nThanks for playing!")
print(f"Final Score: Wins: {wins} | Losses: {losses} | Ties: {ties}")

# Start the game
play_game()
