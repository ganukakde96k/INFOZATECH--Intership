import json
import os
from datetime import datetime

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
    print(f"Date: {datetime.now().strftime('%d-%m-%Y')} | INFOZATECH Internship Task 1")
    print("===== Welcome to INFOZATECH To-Do App =====")
    print("Developed by ganukakde | Thank you @INFOZATECH")
    print("1. Add Task")
    print("2. Show All Tasks")
    print("3. Delete Task")
    print("4. Mark as Done")
    print("5. Exit")

    choice = input(" Enter your choice (1-5): ")

    if choice == '1':
        name = input(" Enter your Task name : ")
        tasks.append(name)
        save()
        print(f"'{name}' saved!")

    elif choice == '2':
        print("\n--- Your Tasks ---")
        if not tasks:
            print("No tasks yet!")
        for i, t in enumerate(tasks, 1):
            print(f"{i}. {t}")

    elif choice == '3':
        print("\n--- Your Tasks ---")
        for i, t in enumerate(tasks, 1):
            print(f"{i}. {t}")
        try:
            num = int(input("which task you want to delete? Enter number: "))
            removed = tasks.pop(num-1)
            save()
            print(f"'{removed}' deleted!")
        except:
            print("Wrong number!")

    elif choice == '4':
        print("\n--- Mark as Done ---")
        for i, t in enumerate(tasks, 1):
            print(f"{i}. {t}")
        num = input("which task you want to mark as done? Enter number: ")
        print(f"✅ Task {num} Marked as Done! ")

    elif choice == '5':
        print("Thank you @INFOZATECH - Exiting...")
        break
