import random   # Import random module to generate random numbers

def number_guessing_game():
    """
    A simple number guessing game.
    The program will randomly choose a number between 1 and 100,
    and the player has to guess it.
    """

    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)

    # Variable to keep track of the number of attempts
    attempts = 0

    print("🎲 Welcome to the Number Guessing Game!")
    print("I have chosen a number between 1 and 100. Can you guess it?")

    # Infinite loop until the player guesses the number correctly
    while True:
        try:
            # Ask user for input
            guess = int(input("Enter your guess: "))
            attempts += 1  # Increase attempt count by 1

            # Check the guess
            if guess < secret_number:
                print("📉 Too low! Try again.")
            elif guess > secret_number:
                print("📈 Too high! Try again.")
            else:
                # Player guessed correctly
                print(f"✅ Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
                break  # Exit loop

        except ValueError:
            # Handle non-integer input
            print("⚠️ Invalid input! Please enter a number.")

# Run the game
if __name__ == "__main__":
    number_guessing_game()
