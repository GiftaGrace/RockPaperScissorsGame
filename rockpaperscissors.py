import random

def rock_paper_scissors():
    print("Welcome to Rock, Paper, Scissors!")
    options = ['rock', 'paper', 'scissors']

    while True:
        # Get the player's choice
        user_choice = input("Enter 'rock', 'paper', or 'scissors' (or 'quit' to exit): ").lower()
        
        if user_choice == 'quit':
            print("Thanks for playing! Goodbye!")
            break
        
        if user_choice not in options:
            print("Invalid choice. Please choose 'rock', 'paper', or 'scissors'.")
            continue

        # Get the computer's choice
        computer_choice = random.choice(options)
        print(f"Computer chose: {computer_choice}")

        # Determine the winner
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'paper' and computer_choice == 'rock') or \
             (user_choice == 'scissors' and computer_choice == 'paper'):
            print("You win!")
        else:
            print("Computer wins!")

if __name__ == "__main__":
    rock_paper_scissors()
