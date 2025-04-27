# Task 1: Perform Basic Mathematical Operations

def take_input():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    return num1, num2

def add_numbers(num1, num2):
    return num1 + num2

def subtract_numbers(num1, num2):
    return num1 - num2

def multiply_numbers(num1, num2):
    return num1 * num2

def divide_numbers(num1, num2):
    if num2 == 0:
        return "Error! Division by zero."
    return num1 / num2

    
def main():
    num1, num2 = take_input()

    print(f"Addition: {add_numbers(num1, num2)}")
    print(f"Subtraction: {subtract_numbers(num1, num2)}")
    print(f"Multiplication: {multiply_numbers(num1, num2)}")
    print(f"Division: {divide_numbers(num1, num2)}")
    
if __name__ == "__main__":
    main()