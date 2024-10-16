import random
import string

def generate_password(length=12):
    if length < 4:
        raise ValueError("Password length must be at least 4")

    # Define character pools
    letters = string.ascii_letters  # A-Z and a-z
    digits = string.digits          # 0-9
    symbols = "!@#$%^&*()-_+="

    # Ensure password contains at least one letter, digit, and symbol
    password = [
        random.choice(letters),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Fill the rest of the password with random choices
    all_characters = letters + digits + symbols
    password += random.choices(all_characters, k=length - 3)

    # Shuffle to avoid predictable patterns
    random.shuffle(password)

    return ''.join(password)

# Example usage
if __name__ == "__main__":
    length = int(input("Enter the desired password length: "))
    print("Generated Password:", generate_password(length))
