# to_do_list.py
def show_menu():
    print("\n--- TO-DO LIST MENU ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Done")
    print("4. Remove Task")
    print("5. Exit from console")

def display_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    for i, (task, done) in enumerate(tasks.items(), 1):
        status = "✓" if done else "✗"
        print(f"{i}. [{status}] {task}")

def main():
    tasks = {}

    while True:
        show_menu()
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            display_tasks(tasks)

        elif choice == '2':
            task = input("Enter the task: ")
            tasks[task] = False
            print("Task added.")

        elif choice == '3':
            task = input("Enter the exact task to be marked as done: ")
            if task in tasks:
                tasks[task] = True
                print("Task marked as done.")
            else:
                print("Task not found.")

        elif choice == '4':
            task = input("Enter the exact task to be removed: ")
            if task in tasks:
                del tasks[task]
                print("Task removed.")
            else:
                print("Task not found.")

        elif choice == '5':
            print("Exiting To-Do List. Thank you")
            break

        else:
            print("Invalid choice entered")

if __name__ == "__main__":
    main()

