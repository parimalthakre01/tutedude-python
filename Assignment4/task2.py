
def write_to_file():
    user_input = input("Enter text to write to the file: ")
    with open('output.txt', 'w') as file:
        file.write(user_input)
    print("Data successfully written to output.txt")
        
def append_to_file():
    user_input = input("Enter additional text to append to the file: ")
    with open('output.txt', 'a') as file:
        file.write(user_input)
    print("Data successfully appended.")
        
def display_final_content():
    print("Final content output.txt:")
    with open('output.txt', 'r') as file:
        for line in file:
            print(f"{line.strip()}")
        
def main():
    write_to_file()
    append_to_file()
    display_final_content()
    
if __name__ == "__main__":
    main()