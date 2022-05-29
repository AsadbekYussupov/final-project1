from tkinter import *
import tkinter, tkinter.constants, tkinter.filedialog
import tkinter as tk


def askopenfile():
        file = tkinter.filedialog.askopenfilename()
        print ("File: " + file)
        
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