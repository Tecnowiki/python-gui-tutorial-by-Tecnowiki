from Tkinter import *
from os import system

"""
This software use a third part software for 'text to speech'
You can download espeak give on the terminal: "sudo apt-get install espeak"
"""

def send():
    command = text.get(1.0, END)
    var = 'espeak -p 60 -s 175 -v it "' + command + '"'
    system(var)

welcome_text = """Benvenuto in SpeakTk
Puoi ascoltare questa frase cliccando sul bottone"""

root = Tk()
root.title("SpeakTk")
root.resizable(False,False)
root.config(bg = "white")
text = Text(root, height = 10, width = 55)
text.insert("1.0", welcome_text)
text.grid(row = 0,column = 0,padx = 15, pady = 15)
bt1 = Button(root, text = "SEND", bg = "white", command = send)
bt1.grid(row = 1,column = 0,padx = 15, pady = 15)
root.mainloop()
