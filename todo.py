# ------------------------------
# To-Do List CLI Application
# ------------------------------
# Features:
# 1. Add a task
# 2. View all tasks
# 3. Mark task as done
# 4. Delete a task
# 5. Save tasks to a file (so data persists)
# 6. Exit program
# ------------------------------

import os

# File where tasks will be saved
TASKS_FILE = "tasks.txt"


# --- Step 1: Helper functions ---

def load_tasks():
    """Load tasks from file (if exists), return as a list of dicts"""
    tasks = []
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            for line in f:
                task, status = line.strip().split("|")
                tasks.append({"task": task, "done": status == "done"})
    return tasks


def save_tasks(tasks):
    """Save tasks to file"""
    with open(TASKS_FILE, "w") as f:
        for t in tasks:
            status = "done" if t["done"] else "not_done"
            f.write(f"{t['task']}|{status}\n")


def show_tasks(tasks):
    """Display the list of tasks"""
    if not tasks:
        print("\n✅ No tasks yet!")
        return
    print("\n📋 To-Do List:")
    for i, t in enumerate(tasks, start=1):
        status = "✔️" if t["done"] else "❌"
        print(f"{i}. {t['task']} [{status}]")


# --- Step 2: Main program loop ---

def todo_app():
    tasks = load_tasks()  # Load existing tasks at start

    while True:
        print("\n=== To-Do List Menu ===")
        print("1. View tasks")
        print("2. Add task")
        print("3. Mark task as done")
        print("4. Delete task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            show_tasks(tasks)

        elif choice == "2":
            new_task = input("Enter new task: ")
            tasks.append({"task": new_task, "done": False})
            save_tasks(tasks)
            print("✅ Task added successfully!")

        elif choice == "3":
            show_tasks(tasks)
            try:
                task_num = int(input("Enter task number to mark as done: ")) - 1
                if 0 <= task_num < len(tasks):
                    tasks[task_num]["done"] = True
                    save_tasks(tasks)
                    print("✔️ Task marked as done!")
                else:
                    print("❌ Invalid task number.")
            except ValueError:
                print("❌ Please enter a valid number.")

        elif choice == "4":
            show_tasks(tasks)
            try:
                task_num = int(input("Enter task number to delete: ")) - 1
                if 0 <= task_num < len(tasks):
                    removed = tasks.pop(task_num)
                    save_tasks(tasks)
                    print(f"🗑️ Task '{removed['task']}' deleted.")
                else:
                    print("❌ Invalid task number.")
            except ValueError:
                print("❌ Please enter a valid number.")

        elif choice == "5":
            print("👋 Exiting... Your tasks are saved!")
            break

        else:
            print("❌ Invalid choice! Please enter 1-5.")


# --- Step 3: Run the app ---

if __name__ == "__main__":
    todo_app()
