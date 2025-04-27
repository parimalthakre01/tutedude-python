import math

def mathematical_operation(n):
    print(f"Square root {math.sqrt(n)}")
    print(f"Logarithm {math.log(n)}")
    print(f"sine: {math.sin(n)}")
    return n 

def main():
    n = int(input("Enter a number: "))
    mathematical_operation(n)

if __name__ == "__main__":
    main()
