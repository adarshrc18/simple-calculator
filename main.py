def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed"
    return a / b

def modulus(a, b):
    return a % b


def calculator():
    while True:
        print("\n===== SIMPLE CALCULATOR =====")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Modulus")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "6":
            print("Exiting calculator... Goodbye!")
            break

        if choice not in ["1", "2", "3", "4", "5"]:
            print("Invalid choice! Please select correct option.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter numeric values.")
            continue

        if choice == "1":
            print("Result:", add(num1, num2))
        elif choice == "2":
            print("Result:", subtract(num1, num2))
        elif choice == "3":
            print("Result:", multiply(num1, num2))
        elif choice == "4":
            print("Result:", divide(num1, num2))
        elif choice == "5":
            print("Result:", modulus(num1, num2))


if __name__ == "__main__":
    calculator()