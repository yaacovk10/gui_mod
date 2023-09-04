import tkinter as tk
from PIL import Image, ImageTk

# Function to load and display the image
def load_image(image_path):
    image = Image.open(image_path)  # Replace with your image path
    photo = ImageTk.PhotoImage(image)
    label.config(image=photo)
    label.image = photo

# Create the Tkinter window
root = tk.Tk()
root.title("Image Viewer")

# Create buttons with different images
load_button_1 = tk.Button(root, text="Load 1st Image", command=lambda: load_image('nature.jpg'))
load_button_1.pack()

load_button_2 = tk.Button(root, text="Load 2nd Image", command=lambda: load_image('caillaux.jpg'))
load_button_2.pack()

# Create a Label widget to display the image (initially empty)
label = tk.Label(root)
label.pack()

# Start the Tkinter main loop
root.mainloop()
