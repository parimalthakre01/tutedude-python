# task is to create a student dict with marks and name, then add or del name with marks
# if name not found then show appropriate messsage 

student_list = {"parimal" : 90, "sachin": 95, "saurabh": 85, "prashant": 80}
def add_new_name(name, marks): 
    # take name and marks as input 
    name = input("Enter name of the student: ")
    marks = input("Enter marks of student: ")
    student_list[name] = marks
    
def remove_name(name):
    name = input("Enter the name to remove: ")
    del(student_list[name])
    

def print_list():
    for name, marks in student_list.items():
        print(name, marks)
        
def main():
    name = input("Enter the student name: ")
    # search the name in dict
    for student_name in student_list:
        if student_name == name:
            print(f"{name} marks are: ", student_list[student_name])
            break
    else:
        print(f"{name} not found.")

if __name__ == "__main__":
    main()
