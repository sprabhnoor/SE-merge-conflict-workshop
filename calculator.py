"""
Simple Calculator Application
A basic calculator that performs arithmetic operations.
"""


def add(a, b):
    """Add two numbers."""
    return a + b


def subtract(a, b):
    """Subtract b from a."""
    return a - b


def multiply(a, b):
    """Multiply two numbers."""
    return a * b


def divide(a, b):
    """Divide a by b."""
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b


def power(a, b):
    """Raise a to the power of b."""
    return a ** b
def modulo(a, b):
    """Return the remainder when a is divided by b."""
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a % b

def power(a, b):
    """Raise a to the power of b."""
    return a ** b



def main():
    """Main function to run the calculator."""
    print("Welcome to the Simple Calculator!")
    print("Operations: +, -, *, /, ^")
    
    try:
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /, ^): ")
        num2 = float(input("Enter second number: "))
        
        if operator == "+":
            result = add(num1, num2)
        elif operator == "-":
            result = subtract(num1, num2)
        elif operator == "*":
            result = multiply(num1, num2)
        elif operator == "/":
            result = divide(num1, num2)
        elif operator == "%":
            result = modulo(num1, num2)
        elif operator == "^":
            result = power(num1, num2)
        elif operator == "^":
            result = power(num1, num2)
        elif operator == "%":
            result = modulo(num1, num2)
        else:
            print("Invalid operator!")
            return
        
        print(f"Result: {result}")
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
