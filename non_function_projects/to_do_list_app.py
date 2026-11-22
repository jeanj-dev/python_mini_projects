# Create a task manager app

# Create list to store tasks
active_tasks = []
completed_tasks = []
deleted_tasks = []

# set a flag variable
working_on_tasks = True

# Ensure user does not enter empty strings
while True:
    task_manager = input("Enter your name: ").strip()
    if task_manager != "":
        break

    print("Wrong input! Enter a name")

# Greet user and show menu options
print(f"Hi {task_manager.title()}, ready to manage some task?!")
print("\nHere are your menu options:")

# Create the menu options
menu_options = {
    1:'Add task',
    2:'View tasks',
    3:'Mark task complete',
    4:'Delete task',
    5:'Exit'
}

while working_on_tasks:
    
    for key, value in menu_options.items():
        print(f"{key} = {value}")

    print() # Skip line

    # Ensure user enters only numbers
    try:
        choice = int(input("Enter a choice (1, 2, 3, 4, 5). "))
    except ValueError:
        print("Wrong input. Number only.\n")
        continue

    # Ensure users enters valid choice    
    if choice not in menu_options:
        print("Invalid choice! Please enter a valid choice from the task menu.\n")

    else:
        if choice == 1:
            while True:
                add_task = input("Add a task: ").strip()
                if add_task != "":
                    break
            
                print("Wrong input! Enter a task.")

            active_tasks.append(add_task)
            print(f"{add_task.title()} was added.\n")

        elif choice == 2:
            if not active_tasks:
                print("\nNo active tasks.")

            # show active and completed tasks  
            else:
                print("\nTasks active:")
                for task in active_tasks:
                    print(task.title())
                
            if not completed_tasks:
                print("\nNo tasks completed yet.")
            else:   
                print("\nTasks completed: ")
                for task_completed in completed_tasks:
                    print(task_completed.title())

            print() 

        # Show if there tasks added before removing them
        elif choice == 3:
            if not active_tasks:
                print("No active tasks.")

           # Show task that needs to be completed
            else:
                print("\nTask to complete:")
                
                task_number = 0
                numbered_tasks  = {}

                for task in active_tasks:
                    task_number += 1
                    numbered_tasks[task_number] = task

                for num, task in numbered_tasks.items():
                    print(f"{num} = {task.title()}")

                # Ensure user enters only numbers
                try:
                    complete_task = int(input("\nEnter a task number to complete: "))
                except ValueError:
                    print("Wrong input. Number only.")
                    continue
                   
                if complete_task not in numbered_tasks.keys():
                    print("Task is either deleted or has already completed.")
                else:
                    task_completed = active_tasks.pop(complete_task - 1)
                    completed_tasks.append(task_completed)
                    print(f"{task_completed.title()} is completed.\n")
            
        # Show if there are tasks added before deleting them
        elif choice == 4:
            if not active_tasks:
                print("No active tasks.")

            else:
                print("\nTask to delete:")

                task_number = 0
                numbered_tasks  = {}

                for task in active_tasks:
                    task_number += 1
                    numbered_tasks[task_number] = task

                for num, task in numbered_tasks.items():
                    print(f"{num} = {task.title()}")

                print()

                try:
                    delete_task = int(input("Enter a task number to delete: "))
                except ValueError:
                    print("Wrong input. Number only.")
                    continue

                if delete_task not in numbered_tasks.keys():
                    print("Task has either been deleted or not been added.\n")
                else:
                    task_deleted = active_tasks.pop(delete_task - 1)
                    deleted_tasks.append(task_deleted)
                    print(f"{task_deleted.title()} is deleted.\n")
                       
        elif choice == 5:
            print(f"Goodbye {task_manager.title()}!")
            working_on_tasks = False    

# Show final tasks completed
if completed_tasks:              
    print("\nTasks completed:")
    for task_completed in completed_tasks:
        print(task_completed.title())

if deleted_tasks:
    print("\nTasks deleted:")
    for deleted_task in deleted_tasks:
        print(deleted_task.title())
    

