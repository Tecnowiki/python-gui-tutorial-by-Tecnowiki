try:
    from Tkinter import *
except:
    from tkinter import *

def cambia():
    if variabile.get() == 0:
        l1.config(text = "On")
    if variabile.get() == 1:
        l1.config(text = "Off")


root = Tk()
root.title("Checkbutton")
l1 = Label(root, text = "")
"""
Il checkbutton restituira' i seguenti valori:
0, nel caso in cui il checkbutton non sia spuntato
1, nel caso in cui il checkbutton sia spuntato
"""
variabile = IntVar()
cb1 = Checkbutton(root,
                  text = "Checkbutton",
                  variable = variabile, 
                  command = cambia)
                  
l1.grid(row = 0, column = 0, padx = 10, pady = 10)
cb1.grid(row = 1, column = 0, padx = 10, pady = 10)
root.mainloop()
