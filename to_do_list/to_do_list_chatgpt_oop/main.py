# main.py

from todo_list import ToDoList
from utils import get_user_choice

def main():
    """Main function to run the to-do list application."""
    todo_app = ToDoList()

    while True:
        user_choice = get_user_choice()
        
        if user_choice == 'add':
            task = input("Enter a task: ")
            todo_app.add_task(task)
        elif user_choice == 'view':
            todo_app.view_tasks()
        elif user_choice == 'remove':
            if not todo_app.tasks:
                print("The to-do list is empty. Nothing to remove.")
            else:
                task_to_remove = input("Enter the task you want to remove: ")
                todo_app.remove_task(task_to_remove)
        elif user_choice == 'exit':
            print("Exiting the to-do list application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter either 'add', 'view', 'remove', or 'exit'.")

# Run the main function if this file is executed directly
if __name__ == "__main__":
    main()
