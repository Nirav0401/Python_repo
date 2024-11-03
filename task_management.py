def task():
    tasks = []
    while True:
        operation = input("Enter the choice: \n1. Add Task\n2. Update Task\n3. Delete Task\n4. View Task\n5. Exit\n")
        if operation == "1":
            total_task = int(input("How many task do you want to add: "))
            for i in range(1, total_task+1):
                ask_task = input("Enter the Task what you want to add: ")
                tasks.append(ask_task)
                print(f"Your Tasks are\n{tasks}")

        elif operation == "2":
            print(f"Your Tasks are\n{tasks}")
            delete_task = input("Enter the task you want to update: ")
            if delete_task in tasks:
                update_task = input("Enter the new task: ")
                ind = tasks.index(delete_task)
                tasks[ind] = update_task
                print(f"Your {update_task} Tasks is updated successfully") 

        elif operation == "3":
            print(f"Your Tasks are\n{tasks}")
            delete_task = input("Enter the task you want to delete: ")
            if delete_task in tasks:
                ind = tasks.index(delete_task)
                tasks[ind] = delete_task
                # tasks.remove(delete_task)
                print(f"Your {delete_task} Tasks is deleted successfully")
            else:
                print(f"Entered Task {delete_task} is not in list")
        
        elif operation == "4":
            print(f"Your Total Tasks are : {tasks}")

        elif operation == "5":
            print("Closing the Program.........")
            break

        else:
            print("Invalid Input")
            
task()

