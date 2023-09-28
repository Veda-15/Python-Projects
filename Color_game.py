from tkinter import *
import random

colours = ["red", "blue", "yellow", "orange", "purple", "green", "black"]

score = 0
timer = 30


def start_game(event):
    global timer
    if timer == 30:
        # starts the count down
        counter()
    #
    next_colour()


def counter():
    global timer
    if timer > 0:
        timer -= 1
        # input_box = Entry(background="gray", width=30, justify="center", borderwidth=3)
        time_lbl.config(text=f"Time left: {str(timer)}")
        # calls the counter function after every 1 sec = 1000 millsec
        time_lbl.after(1000, counter)


def next_colour():
    global score
    global timer

    if timer > 0:
        # makes text entry box active
        input_box.focus_set()
        # checking colour of text is equal to text entered into the box
        if input_box.get().lower() == colours[1]:
            score += 1
        # clear the text in input box
        input_box.delete(0, END)

        random.shuffle(colours)

        # changing the colour of texts
        label.config(foreground=str(colours[1]), text=str(colours[0]))

        # update the score
        score_lbl.config(text=f"Score: {str(score)}")

    else:
        result = Label(root, font=("arial", 20), text =f"Final score: {str(score)}")
        result.pack()


root = Tk()
root.title("ColorGame")
root.geometry("320x250")


head1 = Label(root, font="arial 30 bold", foreground=random.choice(colours), text="COLOR GAME")
head1.pack()
rule = Label(root, text="Recognise the colour of the text", font="arial 15 bold")
rule.pack()
score_lbl = Label(root, font="arial 15", text="Press enter to start")
score_lbl.pack()
time_lbl = Label(root, font="arial 15", text=f"Time start : {str(timer)}")
time_lbl.pack()
label = Label(root, font="arial 20 bold")

input_box = Entry(background="gray", width=30, justify="center", borderwidth=3)
# run the 'startGame' function when the enter key is pressed
root.bind('<Return>', start_game)
label.pack()
input_box.pack()

input_box.focus_set()

root.mainloop()
