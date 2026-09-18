from tkinter import *
from PIL import ImageTk, Image
import os

root = Tk()
root.attributes("-transparentcolor", "white")
img = ImageTk.PhotoImage(Image.open("image.png"))
panel = Label(root, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")
root.mainloop()
