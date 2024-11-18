# Initialize an empty list to store to-do tasks
to_do_list = []

# List of valid user options
user_options = ['add', 'view', 'remove', 'exit']

# Start an infinite loop to keep prompting the user for actions until they choose to exit
while True:
    # Ask the user for their choice, and sanitize the input by stripping whitespace and converting to lowercase
    user_choice = input("Please enter your choice (add/view/remove/exit): ").strip().lower()
    
    # If the user chooses to add a task
    if user_choice == 'add':
        task = input("Enter a task: ").strip()  # Get the task input and remove any extra whitespace
        if task:
            to_do_list.append(task)  # Add the task to the to-do list if it's not empty
            print("Task added successfully!")
        else:
            print("Task cannot be empty.")  # Notify the user if they tried to add an empty task
    
    # If the user chooses to view the list of tasks
    elif user_choice == 'view':
        if not to_do_list:
            print("There is nothing to display.")  # Inform the user if the list is empty
        else:
            print("To-do List:")  # Display each task with its index number
            for index, task in enumerate(to_do_list, start=1):
                print(f"{index}. {task}")
    
    # If the user chooses to remove a task
    elif user_choice == 'remove':
        if not to_do_list:
            print("The to-do list is empty. Nothing to remove.")  # Inform if there are no tasks to remove
        else:
            task_to_remove = input("Enter the task you want to remove: ").strip()
            if task_to_remove in to_do_list:
                to_do_list.remove(task_to_remove)  # Remove the task if found in the list
                print("Task removed successfully!")
            else:
                print("Task not found in the to-do list.")  # Notify if the task is not found
    
    # If the user chooses to exit the program
    elif user_choice == 'exit':
        print("Exiting the to-do list application. Goodbye!")
        break  # Break out of the loop to end the program
    
    # If the user enters an invalid choice
    else:
        print("Invalid choice. Please enter either 'add', 'view', 'remove', or 'exit'.")
a