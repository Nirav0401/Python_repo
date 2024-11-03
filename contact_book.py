contacts = {}

while True:
    print("\nContact Book App")
    print("1. Create Contact")
    print("2. View Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Search Contact")
    print("6. Count Contact")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter your name: ")
        if name in contacts:
            print(f"Contact name {name} already exists")
        else:
            age = input("Enter the Age: ")
            email = input("Enter the Email: ")
            mobile = input("Enter the Mobile Number: ")
            contacts[name] = {"age": {int(age)}, "email": email, "mobile": mobile}
            print(f"Contact name {name} has been successfully created")

    elif choice == "2":
        name = input("Enter Contact Name to View: ")
        if name in contacts:
            contact = contacts[name]
            print(f"Name: {name}, Age: {age}, Mobile Number: {mobile}")
        else:
            print("Contact not found!")

    elif choice == "3":
        name = input("Enter name to update contact: ")
        if name in contacts:
            age = input("Enter the Age: ")
            email = input("Enter the Email: ")
            mobile = input("Enter the Mobile Number: ")
            contacts[name] = {"age": {age}, "email": {email}, "mobile": {mobile}}
        else:
            print("Contact not found!")
    
    elif choice == "4":
        found = False
        name = input("Enter the name to delete contact: ").lower()
        for contact_name in list(contacts.keys()):
            if contact_name.lower() == name:
                del contacts[contact_name]
                print(f"Contact detail for the {name} is successfully deleted")
                found = True
                break
        else:
            print("Contact not found!")

    elif choice == "5":
        search_name = input("Enter the name to Search contact: ")
        found = False
        for name, contact in contacts.items():
            if search_name.lower() in name.lower():
                print(f"Found: name: {name}, age: {age}, mobile: {mobile}, email: {email}")
                found = True
                break
        if not found:
            print("No Contact found with the name")
    
    elif choice == "6":
        print(f"The Number of Contacts in the Contact book: {len(contacts)}")

    elif choice == "7":
        print("Good bye.. Closing the program")
        break
    else:
        print("Invalid Input")