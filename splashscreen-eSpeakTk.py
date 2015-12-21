from Tkinter import *
from time import sleep
from ttk import Progressbar

def splashscreen():
    root = Tk()
    root.geometry("+200+200")
    root.overrideredirect(True)
    root.configure(bg = "white")
    back = PhotoImage(file = "splashscreen.gif")
    l1 = Label(root, image = back, bg = "white")
    scritta = Progressbar(root, orient = "horizontal", mode = "determinate", length = 240)
    scritta.start(30)
    copyright = Label(root, text = "Copyright by lokk3d", bg = "white")
    root.after(3000, root.destroy)
    l1.pack()
    scritta.pack(side  = "left")
    copyright.pack( side = "right")
    root.mainloop()
