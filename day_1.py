# learning at site https://www.pythonguis.com/tutorials/create-gui-tkinter/
# assume we are creating an app
# create a window


import tkinter as tk # hey, it's a built-in package
from PIL import Image, ImageTk

root = tk.Tk() # the app's main/parent window, must be created before any other windows and you can only have one

# make some adjustments
root.title("my small window") # window's title
root.configure(background="light yellow") # window's background colour
# set the window size
root.minsize(200,200) 
root.maxsize(500,500) # when you press maximize, it only goes up to 500x500!
root.geometry("200x200+50+50") # the coordinate for the window on your screen, if not provided, random position
# {width}x{height}+{x_coor}+{y_coor}

# introduce to widget--the name given to a component of the UI
# labels(a basic widget)
# usage: display text or images

tk.Label(root, text="Nothing will work unless you do.").pack()
tk.Label(root, text="- Maya Angelou").pack() # the pack() method make the widget stay on the current window, and make it top-center

image = tk.PhotoImage(file="demo_images\project_logo.png") # only GIF, PGM, PPM, PNG image, no JPG
# for other formats, use the Pillow library
image1 = Image.open(r"demo_images\the_pomodoro_technique.jpg")
image2 = ImageTk.PhotoImage(image1)
tk.Label(root, image=image2).pack()



root.mainloop() # handles mouse and keyboard inputs and communicates with the OS (you can try typing here and they will be in the window!)
