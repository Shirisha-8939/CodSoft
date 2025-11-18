import sys

# In-memory list to store tasks
tasks = []

def show_menu():
    print("\n==== TO-DO LIST MENU ====")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Mark Task as Done")
    print("5. Delete Task")
    print("6. Exit")

def view_tasks():
    if not tasks:
        print("\nNo tasks yet!")
    else:
        print("\nCurrent To-Do List:")
        for idx, (task, done) in enumerate(tasks, 1):
            status = "Done" if done else "Pending"
            print(f"{idx}. {task} [{status}]")

def add_task():
    task = input("Enter task description: ").strip()
    if task:
        tasks.append((task, False))
        print("Task added.")
    else:
        print("Task cannot be empty!")

def update_task():
    view_tasks()
    try:
        task_num = int(input("Enter task number to update: ")) - 1
        if 0 <= task_num < len(tasks):
            new_task = input("Enter the updated description: ").strip()
            if new_task:
                _, done = tasks[task_num]
                tasks[task_num] = (new_task, done)
                print("Task updated.")
            else:
                print("Update cannot be empty!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Enter a valid number.")

def mark_done():
    view_tasks()
    try:
        task_num = int(input("Enter task number to mark as done: ")) - 1
        if 0 <= task_num < len(tasks):
            task, _ = tasks[task_num]
            tasks[task_num] = (task, True)
            print("Task marked as done.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Enter a valid number.")

def delete_task():
    view_tasks()
    try:
        task_num = int(input("Enter task number to delete: ")) - 1
        if 0 <= task_num < len(tasks):
            tasks.pop(task_num)
            print("Task deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Enter a valid number.")

def main():
    while True:
        show_menu()
        choice = input("\nEnter your choice (1-6): ").strip()
        if choice == '1':
            view_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            update_task()
        elif choice == '4':
            mark_done()
        elif choice == '5':
            delete_task()
        elif choice == '6':
            print("Exiting... Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please select 1-6.")

if __name__ == "__main__":
    main()
