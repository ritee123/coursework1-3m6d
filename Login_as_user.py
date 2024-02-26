from tkinter import *
import json
from PIL import Image
from stegano import lsb

def adminlogin_validation(username, password):
    return len(username) != 0 and username != "User Name" and len(password) != 0 and password != "Password"

def userlogin_data_error():
    title = "Error"
    message = "Recheck Your Input\n Values"
    from errors import error as show_error
    show_error(title,message)
    
def userlogin_validation(WIN, phonenumber, password):
    image_path = "images/img.png"
    decoded_data = lsb.reveal(image_path)
    decoded_data = json.loads(decoded_data)

    print("Decoded Data: ", decoded_data)

    for i in decoded_data["users"]:
        if i[2] == phonenumber and str(i[7]) == password:
            print("User Login Success")
            WIN.destroy()
            from user_dashboard import homepage
            homepage()
            return True
    
    print("User Login Failed")
    return False
    

def confirm_user(WIN,user_idtemp_user_id):
    record = [] 

    if userlogin_validation(user_idtemp_user_id):
        WIN.destroy()
        from adduser import viewcandidate
        viewcandidate()
    else:
        userlogin_data_error()


def userlogin():
    WIN = Tk()
    WIN.title('Online Banking System')
    WIN.geometry('360x640')

    background = PhotoImage(file="images/userlogin.png")
    label_background = Label(WIN, image=background, borderwidth=0)
    label_background.place(x=0, y=0)
    w = Canvas(WIN, width=350, height=280, borderwidth=0, highlightthickness=0)
    w.create_rectangle(0, 0, 350, 300, fill="#FFFFFF", outline='#000000')
    w.pack(padx=40, pady=(310,0))
   
    def temp_user_id(e):
        user_id_entry.delete(0, "end")

    user_id_entry = Entry(WIN, font=("Comic Sans MS", 14) , justify="center", width=15, foreground="#AFAFAF")
    user_id_entry.insert(2, "Mobile Number")
    user_id_entry.bind("<FocusIn>", temp_user_id)
    user_id_entry.place(relx=0.5, rely=0.6, anchor=CENTER)


    def temp_password(e):
        '''Clears password_entry to take user input and configured password entry to show * when password is entered.'''
        password_entry.config(show="*")
        password_entry.delete(0, "end")
    password_entry = Entry(WIN, font=("Comic Sans MS", 14) , justify="center", width=15, foreground="#AFAFAF")
    password_entry.insert(0, "Password")
    password_entry.bind("<FocusIn>", temp_password)
    password_entry.place(relx=0.5, rely=0.7, anchor=CENTER)
    userlogin_button = Button(WIN, font=("Comic Sans MS", 14) , justify="center", width=10, borderwidth=0, text="Log In", bg="#645394",command=lambda : userlogin_validate(WIN,user_id_entry.get(),password_entry.get()))
    userlogin_button.place(relx=0.5, rely=0.8, anchor=CENTER)

    WIN.mainloop()

def userlogin_validate(WIN,u,p):
    print("WIN: ", WIN)
    print("username_entry.get(): ", u)
    print("password_entry.get(): ", p)
    userlogin_validation(WIN, u, p)

userlogin()