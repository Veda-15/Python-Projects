from sqlite3 import OperationalError
from tkinter import *

root = Tk()
root.title("Simple Calculator")

#Input box for entering the value
input = Entry(root, state = 'normal',width = 35,borderwidth=8)
input.grid(row=0,column =0 , columnspan= 3 , padx = 10 ,pady = 10)


def button_click(number):
    current = input.get() 
    input.delete(0, END)
    input.insert(0,str(current)+str(number))

def button_clear():
    input.delete(0,END)
    
def button_add():
    global first_num 
    first_num = int(input.get())
    global operation
    operation = "addition"
    input.delete(0,END)

def button_subtract():
    global first_num 
    first_num = int(input.get())
    global operation
    operation = "subtract"
    input.delete(0,END)

def button_multiply():
    global first_num 
    first_num = int(input.get())
    global operation
    operation = "multiply"
    input.delete(0,END)

def button_divide():
    global first_num 
    first_num = int(input.get())
    global operation
    operation = "divide"
    input.delete(0,END)

def button_equal():
    global sec_num
    sec_num = int(input.get())
    input.delete(0,END)
    if operation == "addition":
        input.insert(0,int(first_num)+int(sec_num))
    elif operation == "subtract":
        input.insert(0,int(first_num)-int(sec_num))
    elif operation == "multiply":
        input.insert(0,int(first_num)*int(sec_num))
    else:
        input.insert(0,int(first_num)/int(sec_num))



#creation of buttons
button1 = Button(root , text ="1" ,padx = 30 , pady = 30, command = lambda :button_click(1))
button2 = Button(root , text ="2" ,padx = 30 ,pady = 30, command = lambda :button_click(2))
button3 = Button(root , text ="3" ,padx = 30 , pady = 30, command = lambda :button_click(3))

button4 = Button(root , text ="4" ,padx = 30 , pady = 30, command = lambda :button_click(4))
button5 = Button(root , text ="5" ,padx = 30 , pady = 30, command = lambda :button_click(5))
button6 = Button(root , text ="6" ,padx = 30 , pady = 30, command = lambda :button_click(6))

button7 = Button(root , text ="7" ,padx = 30 , pady = 30, command = lambda :button_click(7))
button8 = Button(root , text ="8" ,padx = 30 , pady = 30, command = lambda :button_click(8))
button9 = Button(root , text ="9" ,padx = 30 , pady = 30, command = lambda :button_click(9))

button0 = Button(root , text ="0" ,padx = 30 , pady = 30, command = lambda :button_click(0))
button_equal = Button(root , text ="=" ,padx = 70 , pady = 30, command = button_equal)
button_clear = Button(root , text ="clear" ,padx = 62 , pady = 30, command = button_clear)

button_add = Button(root,text="+",padx =29 ,pady=30 ,command= button_add)
button_subtract = Button(root,text="-",padx =29 ,pady=30 ,command= button_subtract)
button_multiply = Button(root,text="*",padx =30 ,pady=30 ,command= button_multiply)
button_divide = Button(root,text="/",padx =30 ,pady=30 ,command= button_divide)



button1.grid(row=3,column = 0)
button2.grid(row=3,column = 1)
button3.grid(row=3,column = 2)

button4.grid(row=2,column = 0)
button5.grid(row=2,column = 1)
button6.grid(row=2,column = 2)

button7.grid(row=1,column = 0)
button8.grid(row=1,column = 1)
button9.grid(row=1,column = 2)

button0.grid(row=4,column = 0)
button_add.grid(row=5,column = 0)
button_equal.grid(row =4,column = 1,columnspan=2)
button_clear.grid(row = 5,column = 1,columnspan=2)

button_subtract.grid(row=6,column = 0)
button_multiply.grid(row=6,column = 1)
button_divide.grid(row=6,column = 2)


root.mainloop()