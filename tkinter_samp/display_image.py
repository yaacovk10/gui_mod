import tkinter as tk
from PIL import Image, ImageTk

# Create the Tkinter window
root = tk.Tk()
root.title("Image Viewer")

# Load the image using PIL
image = Image.open("nature.jpg")  # Replace "your_image.png" with the path to your image file

# Convert the PIL image to a PhotoImage object
photo = ImageTk.PhotoImage(image)

# Create a Label widget to display the image
label = tk.Label(root, image=photo)
label.pack()  # You can also use label.grid() if you prefer a grid layout

# Start the Tkinter main loop
root.mainloop()
