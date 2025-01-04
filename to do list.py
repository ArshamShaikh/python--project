from colorama import init, Fore, Style
from tqdm import tqdm
import os
from datetime import datetime

# Initialize colorama
init()

class ToDoList:
    def __init__(self, filename="tasks.txt"):
        self.filename = filename
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        """Load tasks from file."""
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                for line in file:
                    task_id, description, deadline, status = line.strip().split(",")
                    self.tasks.append({
                        "id": int(task_id),
                        "description": description,
                        "deadline": deadline,
                        "status": status
                    })

    def save_tasks(self):
        """Save tasks to file."""
        with open(self.filename, "w") as file:
            for task in self.tasks:
                file.write(f"{task['id']},{task['description']},{task['deadline']},{task['status']}\n")

    def display_menu(self):
        print(Style.BRIGHT + Fore.CYAN + "\n===== To-Do List Menu =====")
        print(Fore.WHITE + "1. Add Task")
        print(Fore.WHITE + "2. View Tasks")
        print(Fore.WHITE + "3. Mark Task as Completed")
        print(Fore.WHITE + "4. Edit Task")
        print(Fore.WHITE + "5. Delete Task")
        print(Fore.WHITE + "6. Show Progress")
        print(Fore.WHITE + "7. Exit")
        print(Style.BRIGHT + Fore.CYAN + "===========================\n")   

    def validate_deadline(self, deadline):
        """Validate deadline format (YYYY-MM-DD)."""
        try:
            datetime.strptime(deadline, "%Y-%m-%d")
            return True
        except ValueError:
            return False

    def add_task(self):
        description = input(Fore.LIGHTBLUE_EX + "Enter task description: ")
        deadline = input(Fore.LIGHTBLUE_EX + "Enter deadline (YYYY-MM-DD): ")
        while not self.validate_deadline(deadline):
            print(Fore.RED + "Invalid date format. Please enter a valid deadline (YYYY-MM-DD).")
            deadline = input(Fore.LIGHTBLUE_EX + "Enter deadline (YYYY-MM-DD): ")
        task_id = len(self.tasks) + 1
        self.tasks.append({"id": task_id, "description": description, "deadline": deadline, "status": "Pending"})
        self.save_tasks()
        print(Fore.GREEN + f"Task '{description}' added with deadline '{deadline}'.")

    def view_tasks(self):
        if not self.tasks:
            print(Fore.YELLOW + "No tasks to display.")
            return
        print(Style.BRIGHT + Fore.CYAN + "\nTo-Do List:")
        print(Fore.LIGHTBLUE_EX + "[Pending]")
        for task in self.tasks:
            if task["status"] == "Pending":
                print(f"{task['id']}. {task['description']} - Deadline: {task['deadline']}")
        print(Fore.LIGHTBLUE_EX + "\n[Completed]")
        completed_tasks = [task for task in self.tasks if task["status"] == "Completed"]
        if not completed_tasks:
            print("No tasks completed yet.")
        else:
            for task in completed_tasks:
                print(f"{task['id']}. {task['description']} - Completed on {task['deadline']}")

    def mark_task_completed(self):
        self.view_tasks()
        try:
            task_num = int(input(Fore.LIGHTBLUE_EX + "Enter task number to mark as completed: "))
            for task in self.tasks:
                if task["id"] == task_num:
                    if task["status"] == "Completed":
                        print(Fore.RED + f"Task '{task['description']}' is already marked as completed.")
                        return
                    task["status"] = "Completed"
                    self.save_tasks()
                    print(Fore.GREEN + f"Task '{task['description']}' marked as completed!")
                    return
            print(Fore.RED + "Invalid task number.")
        except ValueError:
            print(Fore.RED + "Please enter a valid number.")

    def edit_task(self):
        self.view_tasks()
        try:
            task_num = int(input(Fore.LIGHTBLUE_EX + "Enter task number to edit: "))
            for task in self.tasks:
                if task["id"] == task_num:
                    new_description = input(Fore.LIGHTBLUE_EX + "Enter new task description: ")
                    new_deadline = input(Fore.LIGHTBLUE_EX + "Enter new deadline (YYYY-MM-DD): ")
                    while not self.validate_deadline(new_deadline):
                        print(Fore.RED + "Invalid date format. Please enter a valid deadline (YYYY-MM-DD).")
                        new_deadline = input(Fore.LIGHTBLUE_EX + "Enter new deadline (YYYY-MM-DD): ")
                    task["description"] = new_description
                    task["deadline"] = new_deadline
                    self.save_tasks()
                    print(Fore.GREEN + f"Task '{task['id']}' updated successfully.")
                    return
            print(Fore.RED + "Invalid task number.")
        except ValueError:
            print(Fore.RED + "Please enter a valid number.")

    def delete_task(self):
        self.view_tasks()
        try:
            task_num = int(input(Fore.LIGHTBLUE_EX + "Enter task number to delete: "))
            self.tasks = [task for task in self.tasks if task["id"] != task_num]
            # Re-index tasks after deletion
            for idx, task in enumerate(self.tasks):
                task["id"] = idx + 1
            self.save_tasks()
            print(Fore.GREEN + f"Task {task_num} deleted successfully.")
        except ValueError:
            print(Fore.RED + "Please enter a valid number.")

    def show_progress(self):
        total_tasks = len(self.tasks)
        if total_tasks == 0:
            print(Fore.RED + "No tasks to show progress!")
            return
        completed_tasks = sum(1 for task in self.tasks if task["status"] == "Completed")
        progress = (completed_tasks / total_tasks) * 100
        with tqdm(total=100, ncols=70, bar_format="{l_bar}{bar}| {n:.0f}%", colour="green") as pbar:
            pbar.update(progress)
            print(Fore.WHITE + f"Progress: {progress:.2f}% completed")

    def run(self):
        print(Style.BRIGHT + Fore.LIGHTBLUE_EX + "Welcome to Your To-Do List Manager!")
        while True:
            self.display_menu()
            choice = input(Fore.LIGHTBLUE_EX + "Choose an option (1-7): ")
            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.view_tasks()
            elif choice == "3":
                self.mark_task_completed()
            elif choice == "4":
                self.edit_task()
            elif choice == "5":
                self.delete_task()
            elif choice == "6":
                self.show_progress()
            elif choice == "7":
                print(Fore.CYAN + "Goodbye!")
                break
            else:
                print(Fore.RED + "Invalid choice. Please try again.")

if __name__ == "__main__":
    app = ToDoList()
    app.run()
