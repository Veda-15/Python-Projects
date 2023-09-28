from tkinter import *
from tkinter.ttk import *

import time

root = Tk()
root.title("Clock")


def clock_time():
    display_time = time.strftime('%H:%M:%S %p')
    digit_clock.config(text=display_time)
    digit_clock.after(1000, clock_time)


digit_clock = Label(root, font=('arial', 30), foreground='white', background='black')
digit_clock.pack()
clock_time()

root.mainloop()
