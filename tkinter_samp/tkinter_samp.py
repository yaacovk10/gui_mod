import tkinter as tk

# Create a main window
root = tk.Tk()
root.title("Colored Buttons")

# Function to change the label text based on the button clicked
def change_label_color(color):
    label.config(text=f"Button {color.capitalize()} Clicked!", fg=color.lower())

# Create a label widget
label = tk.Label(root, text="Click a colored button:")
label.pack(pady=20)

# Create red button
red_button = tk.Button(root, text="Red", bg="red", fg='black', width= 100,font= 'Arial',  command=lambda: change_label_color("red"))
red_button.pack(pady=5)

# Create green button
green_button = tk.Button(root, text="Green", bg="green", command=lambda: change_label_color("green"))
green_button.pack(pady=5)

# Create blue button
blue_button = tk.Button(root, text="Blue", bg="blue", command=lambda: change_label_color("blue"))
blue_button.pack(pady=5)

# Start the Tkinter event loop
root.mainloop()
