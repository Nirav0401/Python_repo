import os

def create_file(filename):
    try:
        with open(filename, "x") as f:
            print(f"file Name {filename}: Created Successfully!")

    except FileExistsError:
        print(f"File Name {filename} already exists!")

    except Exception as E:
        print("An Error Occurred!")

def View_all_files():
    files = os.listdir()
    if not files:
        print("No file found!")
    else:
        print("files in directory!")
        for file in files:
            print(file)

def Delete_file(filename):
    try:
        os.remove(filename)
        print(f"{filename} has been successfully deleted!")
    except FileNotFoundError:
        print("File not found!")
    except Exception as E:
        print("an Error Occurred!")

def Read_file(filename):
    try:
        with open(filename, "r") as f:
            content = f.read()
            print(f"Content of {filename}: {content}")
    except FileNotFoundError:
        print(f"{filename} is not found!")
    except Exception as E:
        print("an Error Occurred!")

def Edit_file(filename):
    try:
        with open(filename, "a+") as f:
            content = input("Enter data to add: ")
            f.write(content)
            print(f"Content added to the {filename} Successfully")
    except FileNotFoundError:
        print(f"{filename} is not Exists!")
    except Exception as E:
        print("an Error Occurred!")

def main():
    while True:
        print("FILE MANAGEMENT APP")
        print("1. Create a File")
        print("2. View a File")
        print("3. Delete a File")
        print("4. Read a File")
        print("5. Edit a File")
        print("6. Exit")

        choice = int(input("Enter a choice: "))

        if choice == 1:
            filename = input("Enter a filename to Create: ")
            create_file(filename)
        elif choice == 2:
            View_all_files()
        elif choice == 3:
            filename = input("Enter a filename to Delete: ")
            Delete_file(filename)
        elif choice == 4:
            filename = input("Enter a filename to Read: ")
            Read_file(filename)
        elif choice == 5:
            filename = input("Enter a filename to Edit: ")
            Edit_file(filename)
        elif choice == 6:
            print("Closing a program...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()