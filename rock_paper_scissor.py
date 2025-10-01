import random   # Import random to let the computer pick choices

def rock_paper_scissors():
    
    """
      Rock Paper Scissors Game:
    - User enters his choice
    - Computer randomly chooses his choice
    - According to rules you may win loose or may tie
    """
# List of possible moves
choices = ["rock", "paper", "scissors"]

print("🎮 Welcome to Rock, Paper, Scissors!")
print("Type 'quit' to exit the game.\n")

while True:
    # Get user input
    user_choice = input("Enter rock, paper, or scissors: ").lower()

    # Allow user to quit
    if user_choice == "quit":
        print("Thanks for playing! Goodbye 👋")
        break

    # Validate input
    if user_choice not in choices:
        print("❌ Invalid choice! Please try again.")
        continue

    # Computer randomly selects a choice
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    # Determine the winner
    if user_choice == computer_choice:
        print("😲 It's a tie!\n")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("✅ You win!\n")
    else:
        print("💻 Computer wins!\n")
        

if __name__ == "__main__":
    rock_paper_scissors()
