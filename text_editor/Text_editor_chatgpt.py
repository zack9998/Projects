import tkinter as tk

root = tk.Tk()
root.geometry("300x200")

# Create a label in the first row, first column
label = tk.Label(root, text="Enter your name:")
label.grid(column=0, row=0)

# Create an entry (text box) in the first row, second column
entry = tk.Entry(root)
entry.grid(column=1, row=0)

# Create a button in the second row, first column
button = tk.Button(root, text="Submit")
button.grid(column=0, row=1)

root.mainloop()
