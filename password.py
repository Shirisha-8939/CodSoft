import string
import random

def generate_password(length):
    # Define possible characters: lowercase, uppercase, digits, and punctuation
    characters = string.ascii_letters + string.digits + string.punctuation
    # Use random.choice to select 'length' characters randomly
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")
    while True:
        try:
            length = int(input("Enter the desired password length: "))
            if length <= 0:
                print("Please enter a positive integer.")
                continue
            password = generate_password(length)
            print("Generated Password:", password)
            break
        except ValueError:
            print("Invalid input! Please enter a number.")

if __name__ == "__main__":
    main()
