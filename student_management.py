t_grade = {}

# Add a student
def add_student(name, grade):
    student_grade[name] = grade
    print("Added {name} with a {grade}")

# update a student
def update_student(name, grade):
    if name in student_grade:
        student_grade[name] = grade
        print(f"{name} with marks are updated {grade}")
    else:
        print(f"{name} is not found")

# Delete a Student
def delete_student(name):
    if name in student_grade:
        del student_grade[name]
        print(f"{name} has been successfully deleted")
    else:
        print(f"{name} is not found")

# View Student Detail
def display_all_student():
    if student_grade:
        for name, grade in student_grade.items():
            print(f"{name} : {grade}")
    else:
        print("No student found/added")

def main():
    while True:
        print("\nStudent Grades Management System")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. View Student")
        print("5. Exit")

        choice = int(input("Enter your choice: "))
        if choice == 1:
            name = input("Enter Student Name: ")
            grade = int(input("Enter Student marks: "))
            add_student(name, grade)
        elif choice == 2:
            name = input("Enter New Student Name: ")
            grade = int(input("Enter New Student's marks: "))
            update_student(name, grade)

        elif choice == 3:
            name = input("Enter Student Name: ")
            delete_student(name)

        elif choice == 4:
            display_all_student()

        elif choice == 5:
            print("Closing the Program...")
            break

        else:
            print("invalid choice")

if __name__ == "__main__":
    main()