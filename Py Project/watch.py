from tkinter import*
from tkinter.ttk import*
from time import strftime
root = Tk()
root.title("clock")


def time():
    string = strftime("%H:%M:%S:%p")
    lable.config(text=string)
    lable.after(1000, time)


lable = lable(root, fort=("ds-digital", 80),
              background="black", foreground="cyan")
lable.pack(anchr='centre')
time()

mainloop()
