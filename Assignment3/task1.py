def calculate(n):
    if n == 0 or n == 1:
        return 1
    elif n >1 :
        return n * calculate(n-1)
    
    
def main():
    n = int(input("Enter a number: "))
    result = calculate(n)
    print(f"Factorial of {n} is: {result}")
    
if __name__ == "__main__":
    main()