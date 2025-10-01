# 💱 Currency Converter in Python

def currency_converter():
    """
    Simple Currency Converter:
    - User enters an amount in one currency
    - Chooses which currency to convert to
    - Program converts based on predefined exchange rates
    """

    print("💱 Welcome to the Currency Converter!\n")

    # Predefined exchange rates (example values)
    # Base currency: USD
    exchange_rates = {
        "USD": 1.0,        # US Dollar
        "EUR": 0.92,       # Euro
        "INR": 83.1,       # Indian Rupee
        "GBP": 0.79,       # British Pound
        "JPY": 150.5       # Japanese Yen
    }

    # Show available currencies
    print("Available currencies:")
    for currency in exchange_rates.keys():
        print("-", currency)

    try:
        # Ask user for base currency
        from_currency = input("\nEnter the currency you have (e.g., USD): ").upper()

        # Ask user for target currency
        to_currency = input("Enter the currency you want to convert to (e.g., INR): ").upper()

        # Ask user for amount
        amount = float(input(f"Enter the amount in {from_currency}: "))

        # Check if entered currencies are valid
        if from_currency in exchange_rates and to_currency in exchange_rates:
            # Convert amount to USD first, then to target currency
            usd_amount = amount / exchange_rates[from_currency]  #usd_amount = 100 / 83.1 ≈ 1.20 USD
            converted_amount = usd_amount * exchange_rates[to_currency] #converted_amount = 1.20 * 0.92 ≈ 1.10 EUR


            # Print result
            print(f"\n💰 {amount:.2f} {from_currency} = {converted_amount:.2f} {to_currency}")

        else:
            print("⚠️ Invalid currency code! Please choose from the available options.")

    except ValueError:
        print("⚠️ Invalid input! Please enter numeric values for amount.")


# Run the converter
if __name__ == "__main__":
    currency_converter()
