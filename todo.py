import os
FILENAME = "todolist.txt"
def read_tasks():
    tasks = []
    if os.path.isfile(FILENAME):
        with open(FILENAME, "r") as f:
            tasks = [line.strip() for line in f]
    return tasks

def write_tasks(tasks):
    with open(FILENAME, "w") as f:
        for task in tasks:
            f.write(task + "\n")

def display_tasks(tasks):
    if not tasks:
        print("No tasks to do today!")
        return
    print("\n--- TO-DO LIST FOR THE DAY ---")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")
    print()

def add_new_task(tasks):
    new_task = input("Enter task to add: ").strip()
    if new_task:
        tasks.append(new_task)
        write_tasks(tasks)
        print(f"New Task added to list: '{new_task}'")
    else:
        print("Task not added.")

def delete_task(tasks):
    
    display_tasks(tasks)
    if not tasks:
        return
    try:
        choice = int(input("Enter task number to be checked off!: "))
        if 1 <= choice <= len(tasks):
            removed = tasks.pop(choice - 1)
            write_tasks(tasks)
            print(f"Checked off: '{removed}'")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid task.")

def show_menu():
    print("\n----- YOUR TO-DO LIST ------")
    print("1. View pending Tasks")
    print("2. Add a new Task")
    print("3. Checkoff a Task as done")
    print("4. Exit")

def main():
    tasks = read_tasks()
    while True:
        show_menu()
        option = input("Choose an option (1-4): ").strip()

        if option == '1':
            display_tasks(tasks)
        elif option == '2':
            add_new_task(tasks)
        elif option == '3':
            delete_task(tasks)
        elif option == '4':
            print("Closing your TO-DO List!")
            break
        else:
            print("Invalid input. Please choose 1-4.")

if __name__ == "__main__":
    main()
