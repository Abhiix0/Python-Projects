import os


def load_tasks(filename="tasks.txt"):
    tasks = []
    if os.path.exists(filename):
        with open(filename, "r") as f:
            for line in f:
                task, status = line.strip().split(" | ")
                tasks.append({"task": task, "done": status == "done"})
    return tasks

def save_tasks(tasks, filename="tasks.txt"):
    with open(filename, "w") as f:
        for t in tasks:
            status = "done" if t["done"] else "not done"
            f.write(f"{t['task']} | {status}\n")


def add_task(tasks, task):
    tasks.append({"task": task, "done": False})

def remove_task(tasks, index):
    if 0 <= index < len(tasks):
        tasks.pop(index)


def mark_done(tasks, index):
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True


def view_tasks(tasks):
    if not tasks:
        print("No tasks yet.")
    for i, t in enumerate(tasks):
        status = "✅" if t["done"] else "❌"
        print(f"{i}. {t['task']} [{status}]")


def main():
    tasks = load_tasks()
    
    while True:
        print("\n--- To-Do List ---")
        print("1. View tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Mark task as done")
        print("5. Quit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            task = input("Enter task: ")
            add_task(tasks, task)
        elif choice == "3":
            index = int(input("Enter task number to remove: "))
            remove_task(tasks, index)
        elif choice == "4":
            index = int(input("Enter task number to mark done: "))
            mark_done(tasks, index)
        elif choice == "5":
            save_tasks(tasks)
            print("Tasks saved. Bye! 👋")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
