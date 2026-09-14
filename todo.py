"""
Project 1: The To-Do List
DecodeLabs - Industrial Training Kit

Goal: Build a program where users can add tasks to a list and view them.
Key Skill: Lists (append & print loops).

This version also implements PERSISTENCE (saving data to a JSON file on disk),
matching the "Engineering Requires Persistence" concept from the slides,
so tasks are not lost when the program closes (RAM is volatile, Disk is not).
"""

import json
import os

# =========================================================
# MODEL (Data Logic) -> Handles storage & data operations
# =========================================================

DATA_FILE = "tasks.json"


def load_tasks():
    """Load tasks from the JSON file (Disk -> RAM). Returns an empty list if no file exists."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []


def save_tasks(tasks):
    """Save the current tasks list to the JSON file (RAM -> Disk)."""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=4, ensure_ascii=False)


def add_task(tasks, description):
    """Add a new task (a dictionary = a database row) to the list."""
    new_task = {
        "id": len(tasks) + 1,
        "task": description,
        "done": False
    }
    tasks.append(new_task)   # <-- The core skill: list.append()
    save_tasks(tasks)


def view_tasks(tasks):
    """Print all tasks using a for loop with enumerate() (the professional way)."""
    if not tasks:
        print("\nNo tasks yet. Your list is empty!\n")
        return

    print("\n--- YOUR TASKS ---")
    for index, task in enumerate(tasks, start=1):
        status = "✔ Done" if task["done"] else "◻ Pending"
        print(f"{index}. {task['task']}  [{status}]")
    print("------------------\n")


def mark_task_done(tasks, task_number):
    """Mark a task as done by its displayed number."""
    if 1 <= task_number <= len(tasks):
        tasks[task_number - 1]["done"] = True
        save_tasks(tasks)
        print("Task marked as done!\n")
    else:
        print("Invalid task number.\n")


def delete_task(tasks, task_number):
    """Remove a task by its displayed number."""
    if 1 <= task_number <= len(tasks):
        removed = tasks.pop(task_number - 1)
        save_tasks(tasks)
        print(f"Deleted: {removed['task']}\n")
    else:
        print("Invalid task number.\n")


# =========================================================
# VIEW (User Interface) -> Handles user interaction only
# =========================================================

def show_menu():
    print("=" * 30)
    print("   TO-DO LIST - DecodeLabs")
    print("=" * 30)
    print("1. Add a task")
    print("2. View all tasks")
    print("3. Mark a task as done")
    print("4. Delete a task")
    print("5. Exit")


def main():
    tasks = load_tasks()   # load saved data when the program starts

    while True:
        show_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            description = input("Enter the task description: ").strip()
            if description:
                add_task(tasks, description)
                print("Task added successfully!\n")
            else:
                print("Task cannot be empty.\n")

        elif choice == "2":
            view_tasks(tasks)

        elif choice == "3":
            view_tasks(tasks)
            try:
                num = int(input("Enter task number to mark as done: "))
                mark_task_done(tasks, num)
            except ValueError:
                print("Please enter a valid number.\n")

        elif choice == "4":
            view_tasks(tasks)
            try:
                num = int(input("Enter task number to delete: "))
                delete_task(tasks, num)
            except ValueError:
                print("Please enter a valid number.\n")

        elif choice == "5":
            print("Goodbye! Your tasks are saved in tasks.json")
            break

        else:
            print("Invalid choice, please try again.\n")


if __name__ == "__main__":
    main()
