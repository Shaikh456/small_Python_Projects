# 🧮 BMI (Body Mass Index) Calculator

# Function to calculate BMI
def calculate_bmi(weight, height):
    """
    Formula: BMI = weight (kg) / (height (m) ^ 2)
    """
    bmi = weight / (height ** 2)
    return bmi

# Function to check BMI category
def bmi_category(bmi):
    """
    Categories based on WHO standards:
    Underweight: < 18.5
    Normal weight: 18.5 – 24.9
    Overweight: 25 – 29.9
    Obesity: 30 or higher
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obesity"

# Main program
print("⚖️  BMI Calculator")

# Take inputs from user
weight = float(input("Enter your weight in kilograms (kg): "))
height = float(input("Enter your height in meters (m): "))

# Calculate BMI
bmi = calculate_bmi(weight, height)

# Print result
print(f"\nYour BMI is: {bmi:.2f}")
print(f"Category: {bmi_category(bmi)}")
