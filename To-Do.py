import json
from datetime import datetime

TASKS_FILE = "tasks.json"

def main():
    while True:
        print("""
        1. Add tasks
        2. View task
        3. Mark complete
        4. Delete task
        5. Exit
        """)

        choice = int(input("Enter your choice: "))

        match choice:
            case 1:
                title = input("Task: ")
                due_date = input("Due Date(Y-m-d): ")
                if date_validation(due_date):
                    add_tasks(title, due_date)
                    view_tasks()
                else:
                    print("Invalid Due Date")
            case 2:
                view_tasks()
            case 3:
                view_tasks()
                id = input("Enter the tasks id: ")
                mark_complete(id)
                view_tasks()
            case 4:
                view_tasks()
                id = input("Enter the tasks id: ")
                delete_tasks(id)
            case 5:
                print("Exiting...")
                break
            case _:
                print("Invalid choice")

def load_tasks():
    try:
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
def save(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def add_tasks(title, date):
    tasks = load_tasks()
    id = len(tasks) + 1
    task = {
        "id": id,
        "title": title,
        "due_date": date,
        "done": False
    }
    tasks.append(task)
    save(tasks)
    print("Tasks added.")

def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return

    for task in tasks:
        status = "✔" if task["done"] else "✘"
        print(f"\n{task['id']}. {task['title']} | Due Date: {task['due_date']} [{status}]")

def mark_complete(id):
    tasks = load_tasks()

    for task in tasks:
        if task["id"] == int(id):
            task["done"] = True
            save(tasks)
            print("Task marked as complete.")
            return
    print("Task not found.")

def delete_tasks(id):
    tasks = load_tasks()

    for task in tasks:
        if task["id"] == int(id):
            tasks.remove(task)
            save(tasks)
            print("Task deleted.")
            return
    print("Task not found.")

def date_validation(due_date):
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
        return True
    except ValueError:
        return False
            


main()
