import json
import os

# The data file is stored next to this script.
# Some online runners do not define __file__, so fall back to the current folder.
try:
    DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "todo_list.json")
except NameError:
    DATA_FILE = "todo_list.json"


# Load tasks from file (start fresh if the file is missing or damaged)
def load_tasks():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as file:
                return json.load(file)
        except (json.JSONDecodeError, OSError):
            print("Could not read the saved file. Starting with an empty list.\n")
    return {"tasks": [], "completed": []}


# Save tasks to file
def save_tasks(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)


# Turn "1, 3, 5" into a list of valid zero-based positions (highest first)
def parse_numbers(text, size):
    chosen = set()
    ignored = []
    for part in text.split(","):
        part = part.strip()
        if part.isdigit() and 1 <= int(part) <= size:
            chosen.add(int(part) - 1)
        elif part:
            ignored.append(part)
    return sorted(chosen, reverse=True), ignored


# Add multiple tasks
def add_task(data):
    print("Enter tasks you want to add (type 'done' to stop):")
    while True:
        title = input("Task title: ").strip()
        if title.lower() == "done":
            break
        if not title:
            print("Task title cannot be empty.\n")
            continue
        category = input("Enter category (Work/Personal/etc.): ").strip() or "General"
        data["tasks"].append({"title": title, "category": category})
        print("Task added.\n")
    save_tasks(data)


# View pending tasks
def view_tasks(data):
    if not data["tasks"]:
        print("No tasks available.\n")
    else:
        print("\nPending Tasks:")
        for i, task in enumerate(data["tasks"], 1):
            print(f"{i}. {task['title']} [{task['category']}]")
        print()


# Update the title and/or category of one pending task
def update_task(data):
    view_tasks(data)
    if not data["tasks"]:
        return
    number = input("Enter the task number to update: ").strip()
    positions, _ = parse_numbers(number, len(data["tasks"]))
    if len(positions) != 1:
        print("Invalid task number.\n")
        return
    task = data["tasks"][positions[0]]
    new_title = input(f"New title (press Enter to keep '{task['title']}'): ").strip()
    new_category = input(f"New category (press Enter to keep '{task['category']}'): ").strip()
    if new_title:
        task["title"] = new_title
    if new_category:
        task["category"] = new_category
    save_tasks(data)
    print("Task updated.\n")


# Delete multiple pending tasks
def delete_task(data):
    view_tasks(data)
    if not data["tasks"]:
        return
    text = input("Enter task numbers to delete (comma-separated): ")
    positions, ignored = parse_numbers(text, len(data["tasks"]))
    for i in positions:
        data["tasks"].pop(i)
    if positions:
        save_tasks(data)
        print(f"{len(positions)} task(s) deleted.")
    if ignored or not positions:
        print("Some entries were not valid task numbers and were skipped.")
    print()


# Mark multiple tasks as completed
def complete_task(data):
    view_tasks(data)
    if not data["tasks"]:
        return
    text = input("Enter task numbers to mark as completed (comma-separated): ")
    positions, ignored = parse_numbers(text, len(data["tasks"]))
    for i in positions:
        data["completed"].append(data["tasks"].pop(i))
    if positions:
        save_tasks(data)
        print(f"{len(positions)} task(s) marked as completed.")
    if ignored or not positions:
        print("Some entries were not valid task numbers and were skipped.")
    print()


# View completed tasks
def view_completed(data):
    if not data["completed"]:
        print("No completed tasks.\n")
    else:
        print("\nCompleted Tasks:")
        for i, task in enumerate(data["completed"], 1):
            print(f"{i}. {task['title']} [{task['category']}]")
        print()


# Remove multiple completed tasks
def remove_completed(data):
    view_completed(data)
    if not data["completed"]:
        return
    text = input("Enter task numbers to remove (comma-separated): ")
    positions, ignored = parse_numbers(text, len(data["completed"]))
    for i in positions:
        data["completed"].pop(i)
    if positions:
        save_tasks(data)
        print(f"{len(positions)} completed task(s) removed.")
    if ignored or not positions:
        print("Some entries were not valid task numbers and were skipped.")
    print()


# Filter pending tasks by category
def filter_tasks(data):
    category = input("Enter category to filter: ").strip()
    found = False
    print(f"\nTasks in category '{category}':")
    for i, task in enumerate(data["tasks"], 1):
        if task["category"].lower() == category.lower():
            print(f"{i}. {task['title']}")
            found = True
    if not found:
        print("No tasks found in this category.")
    print()


# Main menu
def main():
    data = load_tasks()
    while True:
        print("==== TO-DO LIST MENU ====")
        print("1. Add Task(s)")
        print("2. View Tasks")
        print("3. Update a Task")
        print("4. Delete Task(s)")
        print("5. Complete Task(s)")
        print("6. View Completed Tasks")
        print("7. Remove Completed Task(s)")
        print("8. Filter Tasks by Category")
        print("9. Exit")
        choice = input("Enter your choice (1-9): ").strip()

        if choice == "1":
            add_task(data)
        elif choice == "2":
            view_tasks(data)
        elif choice == "3":
            update_task(data)
        elif choice == "4":
            delete_task(data)
        elif choice == "5":
            complete_task(data)
        elif choice == "6":
            view_completed(data)
        elif choice == "7":
            remove_completed(data)
        elif choice == "8":
            filter_tasks(data)
        elif choice == "9":
            print("Goodbye! Your tasks are saved.")
            break
        else:
            print("Invalid choice. Please try again.\n")


# Run the program
if __name__ == "__main__":
    main()
