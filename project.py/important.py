from tkinter import *
import tkinter, tkinter.constants, tkinter.filedialog
import tkinter as tk
from PIL import Image, ImageTk
import PIL

photos = [
        "download.png",
        "download1.png",
        "download2.png",
        "download3.png",
        "download4.png",
        "download5.png",
        "download6.png",
]

def askopenfile():
        root.file = tkinter.filedialog.askopenfilename(initialdir="/gui/images", title="select a file", filetypes=(("jpg files", "*.jpg"), ("all files", "*.*"), ("png files", "*.png")))
        image = Image.open("download.png")
        image_1 = image.resize((500, 500))
        img = ImageTk.PhotoImage(image_1)
        my_label = Label(root, text=root.file).pack()
                      
                
root = Tk()
root.title("Main Window")
root.geometry("500x500")
root.minsize(500, 500)
root.maxsize(500, 500)

canvas = Canvas(root, width = 200, height = 200)  
    
canvas.pack()
 
img = PhotoImage(file="alatoo.png")
canvas.create_image(35,40, anchor=NW, image=img)    
b = Button(root, text="CLICK HERE\nOPEN FILES", command=askopenfile)
b.pack()



root.mainloop()