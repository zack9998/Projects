# todo_list.py

class ToDoList:
    def __init__(self):
        """Initialize an empty to-do list."""
        self.tasks = []

    def add_task(self, task):
        """Add a task to the to-do list if it's not empty."""
        task = task.strip()
        if task:
            self.tasks.append(task)
            print("Task added successfully!")
        else:
            print("Task cannot be empty.")

    def view_tasks(self):
        """Display all tasks in the to-do list."""
        if not self.tasks:
            print("There is nothing to display.")
        else:
            print("To-do List:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")

    def remove_task(self, task):
        """Remove a task from the to-do list if it exists."""
        task = task.strip()
        if task in self.tasks:
            self.tasks.remove(task)
            print("Task removed successfully!")
        else:
            print("Task not found in the to-do list.")
