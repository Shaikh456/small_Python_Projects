# 💰 Tip Calculator in Python

def tip_calculator():
    """
    Simple Tip Calculator:
    - User enters the bill amount
    - User enters the tip percentage
    - User enters the number of people to split the bill
    - Program calculates total and per-person share
    """

    print("💵 Welcome to the Tip Calculator!")

    try:
        # Ask user for the total bill
        bill = float(input("Enter the total bill amount: $ "))

        # Ask user for tip percentage
        tip_percentage = int(input("Enter tip percentage (e.g., 10, 15, 20): "))

        # Ask how many people will split the bill
        people = int(input("Enter number of people to split the bill: "))

        # Calculate tip amount
        tip_amount = (bill * tip_percentage) / 100

        # Calculate total bill including tip
        total_bill = bill + tip_amount

        # Calculate per-person share
        per_person = total_bill / people

        # Display results
        print("\n--- Calculation Summary ---")
        print(f"Original Bill: ${bill:.2f}")
        print(f"Tip ({tip_percentage}%): ${tip_amount:.2f}")
        print(f"Total Bill (with tip): ${total_bill:.2f}")
        print(f"Each Person Pays: ${per_person:.2f}")

    except ValueError:
        # Handle invalid input (non-numeric values)
        print("⚠️ Please enter valid numbers for bill, tip, and people.")

# Run the calculator
if __name__ == "__main__":
    tip_calculator()
