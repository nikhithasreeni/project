import os
import json


FILENAME = "task.json"

# Load tasks from file into a list
def load_tasks():
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, 'r') as file:
        tasks = [line.strip() for line in file.readlines()]
    return tasks

# Save tasks from the list into the file
def save_tasks(tasks):
    with open(FILENAME, 'w') as file:
        for task in tasks:
            file.write(task + '\n')

# Display all tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        print("\n--- To-Do List ---")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
        print("------------------")

# Add a new task
def add_task(tasks):
    task = input("Enter the new task: ").strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        print("Task added successfully.")
    else:
        print("Task cannot be empty.")

# Update an existing task
def update_task(tasks):
    view_tasks(tasks)
    try:
        index = int(input("Enter the task number to update: ")) - 1
        if 0 <= index < len(tasks):
            new_task = input("Enter the updated task: ").strip()
            if new_task:
                tasks[index] = new_task
                save_tasks(tasks)
                print("Task updated successfully.")
            else:
                print("Updated task cannot be empty.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Delete a task
def delete_task(tasks):
    view_tasks(tasks)
    try:
        index = int(input("Enter the task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            save_tasks(tasks)
            print(f"Task '{removed}' deleted successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Main program loop
def main():
    tasks = load_tasks()

    while True:
        print("\n--- To-Do List Manager ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            update_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("Exiting To-Do List Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please select from 1 to 5.")

if __name__ == "__main__":
    main()
