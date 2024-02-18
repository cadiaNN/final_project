import os

class Task:
    def __init__(self, description, priority, completed=False):
        self.description = description
        self.priority = priority
        self.completed = completed


class ToDoList:
    def __init__(self, file_path):
        self.file_path = file_path
        self.tasks = self.load_tasks()

    def load_tasks(self):
        tasks = []
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                for line in file:
                    description, priority, completed = line.strip().split(',')
                    task = Task(description, int(priority), completed == 'True')
                    tasks.append(task)
        return tasks

    def save_tasks(self):
        with open(self.file_path, 'w') as file:
            for task in self.tasks:
                file.write(f"{task.description},{task.priority},{task.completed}\n")

    def add_task(self, description, priority):
        task = Task(description, priority)
        self.tasks.append(task)
        self.save_tasks()

    def mark_completed(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].completed = True
            self.save_tasks()

    def view_by_priority(self):
        sorted_tasks = sorted(self.tasks, key=lambda x: x.priority)
        for task in sorted_tasks:
            print(f"Priority: {task.priority}, Description: {task.description}, Completed: {task.completed}")

    def remove_completed_tasks(self):
        self.tasks = [task for task in self.tasks if not task.completed]
        self.save_tasks()


# Example usage:
file_path = 'tasks.txt'
to_do_list = ToDoList(file_path)

while True:
    print("\n1. Add Task")
    print("2. Mark Task as Completed")
    print("3. View Tasks by Priority")
    print("4. Remove Completed Tasks")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        description = input("Enter task description: ")
        priority = int(input("Enter priority (number): "))
        to_do_list.add_task(description, priority)

    elif choice == '2':
        index = int(input("Enter the index of the task to mark as completed: "))
        to_do_list.mark_completed(index)

    elif choice == '3':
        to_do_list.view_by_priority()

    elif choice == '4':
        to_do_list.remove_completed_tasks()


    elif choice == '5':
        break

    else:
        print("Invalid choice. Please enter a number (1-5).")

print("Exit to-do list app")
