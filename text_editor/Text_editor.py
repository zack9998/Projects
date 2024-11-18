import tkinter as tk
from tkinter import filedialog

# Function to open a file and display its content in the text box
def open_file():
    # Open a file dialog to select a file
    file_path = filedialog.askopenfilename()
    if file_path:  # Check if a file was selected
        with open(file_path, "r") as file:
            content = file.read()  # Read file content
            text_box.delete(1.0, tk.END)  # Clear current text in the text box
            text_box.insert(tk.END, content)  # Insert file content into the text box

# Function to save the content of the text box to a file
def save_file():
    # Open a file dialog to specify the save location and file name
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    if file_path:  # Check if a file path was specified
        with open(file_path, "w") as file:
            content = text_box.get(1.0, tk.END)  # Get all text from the text box
            file.write(content)  # Write the text to the file

# Initialize the main window
root = tk.Tk()
root.title("Almadrasa Text Editor")  # Set window title
root.geometry("300x300")  # Set default window size

# Create a frame to hold the buttons on the left side
button_frame = tk.Frame(root)
button_frame.pack(side="left", fill="y", padx=5, pady=5)  # Pack the frame on the left side

# Create an "Open File" button and add it to the button frame
open_button = tk.Button(button_frame, text="Open File", command=open_file)
open_button.pack(fill="x", pady=5)  # Make the button fill the frame's width

# Create a "Save File" button and add it to the button frame
save_button = tk.Button(button_frame, text="Save File", command=save_file)
save_button.pack(fill="x", pady=5)  # Make the button fill the frame's width

# Create a text box for editing and displaying text content
text_box = tk.Text(root, wrap="word")  # Enable word wrapping in the text box
text_box.pack(side="right", fill="both", expand=True)  # Pack text box to fill remaining space

# Run the main event loop to keep the application open
root.mainloop()
