import random
import string

def generate_password(length=12):
    """Generate a random password with letters, digits, and symbols."""
    if length < 6:
        print("Password length should be at least 6 characters for better security.")
        return None
    
    # Character sets
    letters = string.ascii_letters   # a-z, A-Z
    digits = string.digits           # 0-9
    symbols = string.punctuation     # !@#$%^&*() etc.
    
    # Ensure at least one character from each category
    password = [
        random.choice(letters),
        random.choice(digits),
        random.choice(symbols)
    ]
    
    # Fill the rest with a mix of all
    all_chars = letters + digits + symbols
    password += random.choices(all_chars, k=length - 3)
    
    # Shuffle so order is random
    random.shuffle(password)
    
    return "".join(password)

# Run the program
if __name__ == "__main__":
    length = int(input("Enter desired password length: "))
    password = generate_password(length)
    if password:
        print("Generated Password:", password)
