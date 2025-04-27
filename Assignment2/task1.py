
def check_even_odd(num):
    if num % 2 == 0:
        return f"{num} is an even number"
    else:
        return f"{num} is an odd number"

def main():
    number = int(input("Enter a number: "))
    result = check_even_odd(number)
    print(result)
    
if __name__ == "__main__":
    main()