# Simple To-Do List App

tasks = []

def display_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        for idx, task in enumerate(tasks, 1):
            status = "Completed" if task['completed'] else "Incomplete"
            print(f"{idx}. {task['title']} - {status}")

def add_task():
    title = input("Enter the task title: ")
    tasks.append({"title": title, "completed": False})
    print(f"Task '{title}' added!")

def edit_task():
    display_tasks()
    task_no = int(input("Enter the task number to edit: ")) - 1
    if 0 <= task_no < len(tasks):
        new_title = input("Enter the new title: ")
        tasks[task_no]['title'] = new_title
        print("Task updated successfully.")
    else:
        print("Invalid task number.")

def delete_task():
    display_tasks()
    task_no = int(input("Enter the task number to delete: ")) - 1
    if 0 <= task_no < len(tasks):
        removed_task = tasks.pop(task_no)
        print(f"Task '{removed_task['title']}' deleted.")
    else:
        print("Invalid task number.")

def mark_completed():
    display_tasks()
    task_no = int(input("Enter the task number to mark as completed: ")) - 1
    if 0 <= task_no < len(tasks):
        tasks[task_no]['completed'] = True
        print(f"Task '{tasks[task_no]['title']}' marked as completed.")
    else:
        print("Invalid task number.")

def menu():
    while True:
        print("\nTo-Do List Menu:")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Edit Task")
        print("4. Delete Task")
        print("5. Mark Task as Completed")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            display_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            edit_task()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            mark_completed()
        elif choice == '6':
            print("Exiting the program...")
            break
        else:
            print("Invalid choice! Please try again.")

menu()
