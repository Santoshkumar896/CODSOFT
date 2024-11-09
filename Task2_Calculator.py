import math

def calculator():
    print("Enhanced Calculator")
    print("Select operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exponentiation (^)")
    print("6. Square Root (√)")
    print("7. Modulo (%)")
    print("8. Factorial (!)")
    print("9. Power (x^y)")

    # Get operation choice from user
    choice = input("Enter choice (1-9): ")

    # Basic operations
    if choice in ['1', '2', '3', '4', '5', '7', '9']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            result = num1 + num2
            print(f"{num1} + {num2} = {result}")
        elif choice == '2':
            result = num1 - num2
            print(f"{num1} - {num2} = {result}")
        elif choice == '3':
            result = num1 * num2
            print(f"{num1} * {num2} = {result}")
        elif choice == '4':
            if num2 != 0:
                result = num1 / num2
                print(f"{num1} / {num2} = {result}")
            else:
                print("Error: Division by zero is not allowed.")
        elif choice == '5':
            result = num1 ** num2
            print(f"{num1} ^ {num2} = {result}")
        elif choice == '7':
            result = num1 % num2
            print(f"{num1} % {num2} = {result}")
        elif choice == '9':
            result = math.pow(num1, num2)
            print(f"{num1} ^ {num2} = {result}")

    # Square root
    elif choice == '6':
        num = float(input("Enter number: "))
        if num >= 0:
            result = math.sqrt(num)
            print(f"√{num} = {result}")
        else:
            print("Error: Square root of a negative number is not real.")

    # Factorial
    elif choice == '8':
        num = int(input("Enter an integer: "))
        if num >= 0:
            result = math.factorial(num)
            print(f"{num}! = {result}")
        else:
            print("Error: Factorial of a negative number is not defined.")

    else:
        print("Invalid input! Please select a valid operation.")

# Run the calculator
calculator()
