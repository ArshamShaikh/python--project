from colorama import init, Fore, Style
from tqdm import tqdm

# Initialize colorama
init()

class ToDoList:
    def __init__(self):
        self.tasks = []  # List of task dictionaries

    def display_menu(self):
        print(Style.BRIGHT + Fore.CYAN + "\n===== To-Do List Menu =====")
        print(Fore.MAGENTA + "1. Add a Task")
        print(Fore.MAGENTA + "2. Mark Task as Completed")
        print(Fore.MAGENTA + "3. View Tasks")
        print(Fore.MAGENTA + "4. Show Progress")
        print(Fore.MAGENTA + "5. Exit")
        print(Style.BRIGHT + Fore.CYAN + "===========================\n")

    def add_task(self):
        task_name = input(Fore.LIGHTBLUE_EX + "Enter the task name: ")
        priority = input(Fore.LIGHTBLUE_EX + "Set priority (High, Medium, Low): ").capitalize()
        self.tasks.append({"task": task_name, "priority": priority, "completed": False})
        print(Fore.GREEN + f"Task '{task_name}' added with priority '{priority}'.")

    def complete_task(self):
        if not self.tasks:
            print(Fore.YELLOW + "No tasks to mark as completed.")
            return
        self.show_tasks()
        try:
            task_num = int(input(Fore.LIGHTBLUE_EX + "Enter task number to mark as completed: ")) - 1
            if 0 <= task_num < len(self.tasks):
                self.tasks[task_num]["completed"] = True
                print(Fore.GREEN + f"Task '{self.tasks[task_num]['task']}' marked as completed!")
            else:
                print(Fore.RED + "Invalid task number.")
        except ValueError:
            print(Fore.RED + "Please enter a valid number.")

    def show_tasks(self):
        if not self.tasks:
            print(Fore.YELLOW + "No tasks to display.")
            return
        print(Style.BRIGHT + Fore.CYAN + "\nYour Tasks:")
        for i, task in enumerate(self.tasks, start=1):
            status = "✅" if task["completed"] else "❌"
            priority_color = Fore.RED if task["priority"] == "High" else Fore.YELLOW if task["priority"] == "Medium" else Fore.GREEN
            print(f"{i}. {priority_color}{task['task']} [{task['priority']}] - {status}")

    def show_progress(self):
        total_tasks = len(self.tasks)
        if total_tasks == 0:
            print(Fore.RED + "No tasks to show progress!")
            return
        completed_tasks = sum(task["completed"] for task in self.tasks)
        progress = (completed_tasks / total_tasks) * 100
        with tqdm(total=100, ncols=70, bar_format="{l_bar}{bar}| {n:.0f}%", colour="green") as pbar:
            pbar.update(progress)
            print(Fore.MAGENTA + f"Progress: {progress:.2f}% completed")

    def run(self):
        print(Style.BRIGHT + Fore.LIGHTBLUE_EX + "Welcome to Your To-Do List Manager!")
        while True:
            self.display_menu()
            choice = input(Fore.LIGHTBLUE_EX + "Choose an option (1-5): ")
            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.complete_task()
            elif choice == "3":
                self.show_tasks()
            elif choice == "4":
                self.show_progress()
            elif choice == "5":
                print(Fore.CYAN + "Goodbye!")
                break
            else:
                print(Fore.RED + "Invalid choice. Please try again.")

if __name__ == "__main__":
    app = ToDoList()
    app.run()
