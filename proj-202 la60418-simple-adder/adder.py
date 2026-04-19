API_KEY = "sk-hardcoded-1234"

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print(f"The sum is: {num1 + num2}")
except ValueError:
    print("Invalid input. Please enter numeric values.")
