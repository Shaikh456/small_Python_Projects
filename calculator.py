# Simple Calculator in Python with Comments

# --- Step 1: Define functions for operations ---

def add(x, y):
    """Return the sum of x and y"""
    return x + y

def subtract(x, y):
    """Return the difference of x and y"""
    return x - y

def multiply(x, y):
    """Return the product of x and y"""
    return x * y

def divide(x, y):
    """Return the division of x by y, with zero-check"""
    if y == 0:
        return "Error! Division by zero."  # Prevent crash if divisor is 0
    return x / y


# --- Step 2: Main calculator logic ---

def calculator():
    # Display menu
    print("=== Python Calculator ===")
    print("Select operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Exit")

    # Loop until user chooses Exit
    while True:
        # Ask user to select an operation
        choice = input("\nEnter choice (1/2/3/4/5): ")

        # If user selects exit
        if choice == "5":
            print("Exiting... Goodbye!")
            break  # End the loop and program

        # If valid choice (1-4), ask for numbers
        if choice in ("1", "2", "3", "4"):
            try:
                # Convert inputs to float (to support decimals too)
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                # Handle case where user enters something that isn’t a number
                print("Invalid input! Please enter numbers only.")
                continue

            # Perform calculation based on choice
            if choice == "1":
                print(f"Result: {num1} + {num2} = {add(num1, num2)}")
            elif choice == "2":
                print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
            elif choice == "3":
                print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")
            elif choice == "4":
                print(f"Result: {num1} / {num2} = {divide(num1, num2)}")

        # If user enters an invalid choice
        else:
            print("Invalid choice! Please select 1-5.")


# --- Step 3: Run the program ---

if __name__ == "__main__":
    calculator()
