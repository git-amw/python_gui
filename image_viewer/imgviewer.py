from tkinter import *
from PIL import ImageTk, Image

root = Tk();

root.title("Image viewer")
#root.geometry("1000x2000")

img1 = ImageTk.PhotoImage(Image.open("images.jpg"))
img2 = ImageTk.PhotoImage(Image.open("a.jpg"))
img3 = ImageTk.PhotoImage(Image.open("b.jpg"))
img4 = ImageTk.PhotoImage(Image.open("c.jpg"))
img5 = ImageTk.PhotoImage(Image.open("d.jpg"))

img_list = [img1, img2, img3, img4, img5]

my_label = Label(image = img1)
my_label.grid(row = 0, column = 0, columnspan = 3)

l = 0

def forward() :
    global l
    global my_label
    global b_for
    global b_back
    b_back["state"] = NORMAL
    l += 1
    my_label.grid_forget()
    my_label = Label(image = img_list[l])
    my_label.grid(row = 0, column = 0, columnspan = 3)
    
    if (l == 4) :
        b_for["state"] = DISABLED
        
def backword() :
    global l
    global my_label
    global b_back
    l -= 1

    my_label.grid_forget()
    my_label = Label(image = img_list[l])
    my_label.grid(row = 0, column = 0, columnspan = 3)
    
    if (l == 0) :
        b_back["state"] = DISABLED
   
    
b_back = Button(root, text = "<<", state = DISABLED, command = backword)
b_exit = Button(root, text = "EXIT", command = root.destroy)
b_for  = Button(root, text = ">>", command = forward)


b_back.grid(row = 1, column = 0)
b_exit.grid(row = 1, column = 1)
b_for.grid(row = 1, column = 2)


root.mainloop()
