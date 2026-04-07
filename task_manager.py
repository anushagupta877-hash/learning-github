tasks = []

while True:
    print("\nStudent Task Manager")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter the task: ")
        tasks.append(task)
        print("Task added successfully!")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, 1):
                print(i, "-", task)

    elif choice == "3":
        task_num = int(input("Enter task number to remove: "))
        if 0 < task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            print("Removed task:", removed)
        else:
            print("Invalid task number.")

    elif choice == "4":
        print("Exiting Task Manager.")
        break

    else:
        print("Invalid choice. Try again.")
