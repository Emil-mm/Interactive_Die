from tkinter import *
import random
from PIL import ImageTk,Image

def spin(button, imageList):
    num = random.randrange(0,6) #Randomly picks an image
    button.config(image=imageList[num])

    
root = Tk()
label = Label(root, text="Roll The Die", font=(("Times New Roman"),12))
#label.grid(row=0, column=0)
label.pack()

#Adding images in list
face1 = ImageTk.PhotoImage(Image.open("face1.png"))
face2 = ImageTk.PhotoImage(Image.open("face2.png"))
face3 = ImageTk.PhotoImage(Image.open("face3.png"))
face4 = ImageTk.PhotoImage(Image.open("face4.png"))
face5 = ImageTk.PhotoImage(Image.open("face5.png"))
face6 = ImageTk.PhotoImage(Image.open("face6.png"))

images = [face1,face2,face3,face4,face5,face6]

dieFace = Button(image=face1, padx=28, pady=20, command=lambda: spin(dieFace, images))
#dieFace.grid(row=1, column=0)
dieFace.pack()

root.mainloop()
