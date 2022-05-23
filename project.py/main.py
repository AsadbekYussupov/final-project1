from tkinter import *

class Window:
    window = Tk()
    logo = PhotoImage(file="Logo.png")


    window.title('final_project')
    window.geometry("600x600+450+0")
    window.minsize(600, 600)
    window.maxsize(600, 600)

    lbl = Label(window, text="Hello")
    lbl.grid(column=20, row=50)
    window.mainloop()
    
Window()