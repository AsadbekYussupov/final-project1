import tkinter as tk
from PIL import ImageTk, Image

        
Files = ["download1.jpg", 
        "download2.jpg",
        "download3.jpg",
        "download4.jpg",
        "download5.jpg",
        "download6.jpg"]      

root = tk.Tk()
root.title("first image")
root.geometry("800x800")

root1 = tk.Toplevel()
root1.title("seocnd image")
root1.geometry("800x800")

image = Image.open("down.jpg")
image1 = Image.open("download1.jpg")

image_ = image.resize((800, 800))
image_1 = image1.resize((800, 800))

image2 = image_.convert("L")

img = ImageTk.PhotoImage(image2)
img_1 = ImageTk.PhotoImage(image_1)

def window():
    im_testlabel = tk.Label(root, image=img)
    im_testlabel.pack()
    im1_testlabel = tk.Label(root1, image=img_1)
    im1_testlabel.pack()
    

    
    
window()
root.mainloop()
root1.mainloop() 
 
#check photo's sizes and resize in app
#combine with window important.py
#try to finish project