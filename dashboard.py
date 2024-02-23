from tkinter import *

def dashboard():
    WIN = Tk()
    WIN.title('Online Banking System')
    WIN.geometry('360x640')
    background = PhotoImage(file="images/DaBank.png")
    label_background = Label(WIN,image=background,borderwidth=0)
    label_background.place(x=0,y=0)

 
    def admin_page():
        WIN.destroy()
        from adminloginfirst import adminlogin as adminlogin
        adminlogin()

    def user_page():
        WIN.destroy()
        from Login_as_user import userlogin as open_register
        open_register()

    def on_enter_admin_login(e):
        admin_login_button.config(background='#7409EB')

  
    def on_leave_admin_login(e):
        admin_login_button.config(background= '#645394')

 
    admin_login_button = Button(WIN,text="Login as Admin",
                                padx=15,borderwidth=0,  font=("Comic Sans MS", 16),
                                 background='#645394', foreground= 'white',command=admin_page)
    admin_login_button.place(relx=0.5, rely=0.7, anchor=CENTER)

    admin_login_button.bind('<Enter>',on_enter_admin_login)
    admin_login_button.bind('<Leave>',on_leave_admin_login)


    def on_enter_user_login(e):
        user_login_button.config(background='#7409EB')

  
    def on_leave_user_login(e):
        user_login_button.config(background= '#645394')
     
    user_login_button = Button(WIN,text="Login as User",padx=15, borderwidth=0,
                                font=("Comic Sans MS", 16), background='#645394',
                                 foreground= 'white',command=user_page)
    user_login_button.place(relx=0.5, rely=0.8, anchor=CENTER)

    user_login_button.bind('<Enter>',on_enter_user_login)
    user_login_button.bind('<Leave>',on_leave_user_login)


    WIN.mainloop()

dashboard()
