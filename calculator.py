import math

# Function definitions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

def power(x, y):
    return x ** y

def modulus(x, y):
    if y == 0:
        return "Error! Modulus by zero."
    else:
        return x % y

def square_root(x):
    if x < 0:
        return "Error! Square root of negative number."
    else:
        return math.sqrt(x)

def absolute_value(x):
    return abs(x)

def calculator():
    while True:
        print("\nEnhanced Calculator Options:")
        print("1. Add (+)")
        print("2. Subtract (-)")
        print("3. Multiply (*)")
        print("4. Divide (/)")
        print("5. Power (^)")
        print("6. Modulus (%)")
        print("7. Square Root (√)")
        print("8. Absolute Value (abs)")
        print("0. Exit")

        choice = input("Enter choice (0-8): ")

        if choice == '0':  # Exit
            confirm = input("Are you sure you want to exit? (yes/no): ").lower()
            if confirm == 'yes':
                print("Goodbye!")
                break

        elif choice in ['1', '2', '3', '4', '5', '6']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input! Please enter numeric values.")
                continue

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                print(f"{num1} / {num2} = {divide(num1, num2)}")
            elif choice == '5':
                print(f"{num1} ^ {num2} = {power(num1, num2)}")
            elif choice == '6':
                print(f"{num1} % {num2} = {modulus(num1, num2)}")

        elif choice == '7':  # Square root of single number
            try:
                num = float(input("Enter number for square root: "))
            except ValueError:
                print("Invalid input! Please enter a numeric value.")
                continue
            print(f"√{num} = {square_root(num)}")

        elif choice == '8':  # Absolute value of single number
            try:
                num = float(input("Enter number for absolute value: "))
            except ValueError:
                print("Invalid input! Please enter a numeric value.")
                continue
            print(f"|{num}| = {absolute_value(num)}")

        else:
            print("Invalid choice! Please select a valid option between 0 and 8.")

# Run the calculator program
calculator()
