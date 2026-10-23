import json
import os

FILE = "tasks.json"

# Load old tasks
if os.path.exists(FILE):
    with open(FILE, "r") as f:
        try:
            tasks = json.load(f)
        except:
            tasks = []
else:
    tasks = []

def save():
    with open(FILE, "w") as f:
        json.dump(tasks, f)

while True:
    print("\n--- MY TO-DO LIST ---")
    print("1. Add Task")
    print("2. Show All Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input(" Enter your choice (1-4): ")

    if choice == '1':
        name = input(" Enter your Task name : ")
        tasks.append(name)
        save()
        print(f"'{name}' saved!")

    elif choice == '2':
        if len(tasks) == 0:
            print("\n>> There are no tasks to display! first add some tasks press 1.")
        else:
            print("\n Your Tasks:")
            for i, t in enumerate(tasks):
                print(f"{i+1}. {t}")

    elif choice == '3':
        num = int(input("which task you want to delete? "))
        if 1 <= num <= len(tasks):
            tasks.pop(num-1)
            save()
            print("Task deleted!")
        else:
            print("Invalid task number!")

    elif choice == '4':
        break