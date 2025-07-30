import os

FILE_NAME = "tasks.txt"

# Load tasks from file
def load_tasks():
    tasks = []
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            for line in f:
                task, status = line.strip().split("|")
                tasks.append({"task": task, "done": status == "done"})
    return tasks

# Save tasks to file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as f:
        for task in tasks:
            status = "done" if task["done"] else "pending"
            f.write(f"{task['task']}|{status}\n")

# Display tasks
def show_tasks(tasks):
    if not tasks:
        print("No tasks yet!")
        return
    print("\n--- Your To-Do List ---")
    for i, task in enumerate(tasks, 1):
        status = "✅" if task["done"] else "❌"
        print(f"{i}. {task['task']} [{status}]")

# Add new task
def add_task(tasks):
    task = input("Enter a new task: ").strip()
    if task:
        tasks.append({"task": task, "done": False})
        print("Task added.")


def mark_done(tasks):
    show_tasks(tasks)
    try:
        index = int(input("Enter task number to mark as done: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["done"] = True
            print("Task marked as done.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def delete_task(tasks):
    show_tasks(tasks)
    try:
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            print(f"Deleted task: {removed['task']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def main():
    tasks = load_tasks()

    while True:
        print("\n--- To-Do Menu ---")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid option. Please choose from 1-5.")

if __name__ == "__main__":
    main()
