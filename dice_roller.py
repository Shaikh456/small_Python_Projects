# ------------------------------
# Dice Roller CLI in Python
# ------------------------------
# Features:
# 1. Roll one or multiple dice
# 2. Choose number of sides (default: 6)
# 3. Exit option
# ------------------------------

import random

def roll_dice(num_dice=1, sides=6):
    """Roll the dice and return results as a list"""
    return [random.randint(1, sides) for _ in range(num_dice)]

def dice_app():
    print("🎲 Welcome to Dice Roller!")
    
    while True:
        print("\n--- Menu ---")
        print("1. Roll a dice (default 6 sides)")
        print("2. Roll multiple dice")
        print("3. Exit")
        
        choice = input("Enter choice (1/2/3): ")
        
        if choice == "1":
            result = roll_dice()
            print(f"🎲 You rolled: {result[0]}")
        
        elif choice == "2":
            try:
                num_dice = int(input("How many dice? "))
                sides = int(input("How many sides per dice (e.g., 6, 8, 12, 20)? "))
                results = roll_dice(num_dice, sides)
                print(f"🎲 Results: {results}")
                print(f"Total sum: {sum(results)}")
            except ValueError:
                print("❌ Please enter valid numbers.")
        
        elif choice == "3":
            print("👋 Goodbye! Thanks for playing.")
            break
        
        else:
            print("❌ Invalid choice! Please select 1, 2, or 3.")

# Run the dice roller
if __name__ == "__main__":
    dice_app()
