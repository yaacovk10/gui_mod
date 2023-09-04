import tkinter as tk
from tkinter import Menu

def save_to_file():
    content = text_widget.get(1.0, tk.END)  # Get the text from the Text widget
    with open("output.txt", "w") as file:
        file.write(content)
    status_label.config(text="File saved successfully!")

def show_save_button():
    save_button.pack()

root = tk.Tk()
root.title("New File")

# Set the size of the main window
root.geometry("400x300")

# Create a Text widget for text input
text_widget = tk.Text(root, wrap=tk.WORD, width=40, height=10)
text_widget.pack()

# Create a hidden Button for saving
save_button = tk.Button(root, text="Save", command=save_to_file)
save_button.pack_forget()

# Create a Label to display the status message
status_label = tk.Label(root, text="")
status_label.pack()

# Create a Menu
menubar = Menu(root)
root.config(menu=menubar)

# Create a "File" menu
filemenu = Menu(menubar)
menubar.add_cascade(label="File", menu=filemenu)

# Add an option to show the save button
filemenu.add_command(label="Show Save Button", command=show_save_button)

root.mainloop()
