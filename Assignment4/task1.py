# Problem Statement:  Write a Python program that:
# 1.   Opens and reads a text file named sample.txt.
# 2.   Prints its content line by line.
# 3.   Handles errors gracefully if the file does not exist.

def read_file():
    try:
        i = 1
        with open('sample.txt', 'r') as file:
            for line in file:
                print(f"Line {i}: {line.strip()}")
                i = i + 1
    except FileNotFoundError:
        print("Error: The file 'sample.txt' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}") 

def main():
    read_file()
    
if __name__ == "__main__":
    main()