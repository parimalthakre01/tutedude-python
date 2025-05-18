my_list = []
def create_list():
    for i in range (1, 11):
        my_list.append(i)
    print(my_list)
    return my_list
    
def first_5_number_and_reverse():
    short_list = my_list[:5]
    print(f"Extracted first five elements: {short_list}")
    reverse_list = sorted(short_list, reverse=True)
    print(f"Reversed extracted elements: {reverse_list}")

    
def main():
    create_list()
    first_5_number_and_reverse()
    
if __name__ == "__main__":
    main()


    