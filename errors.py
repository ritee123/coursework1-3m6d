from tkinter import Button, Label, Toplevel


def error(title,message):
    WIN_top = Toplevel(bg='#E0D9EF')
    WIN_top.title(title)
    WIN_top.geometry('300x150')
    tfont_tup = ("Comic Sans MS", 15)
    def no():
        WIN_top.destroy()
    message = Label(WIN_top, bg='#E0D9EF', text=message, font=("Comic Sans MS", 15), justify="center",
                        foreground="#000000")
    message.pack()
    no_button = Button(WIN_top, bg='#FFFFFF', text=" Ok ", background='Red', foreground="Black", font=("Comic Sans MS", 12), command=no)
    no_button.place(x=108, y=80)

    WIN_top.mainloop()
