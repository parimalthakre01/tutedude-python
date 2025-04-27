def greet_people(first_name: str, last_name: str):
    """Greet the user with their first and last name."""
    print(f"Hello, {first_name} {last_name}! Welcome to python program.")
    
def main():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    greet_people(first_name, last_name)

if __name__ == "__main__":
    main()    