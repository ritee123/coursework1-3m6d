
from tkinter import *


def dashboard_call(WIN):
    '''Destroys the tkinter window and call open function i.e. login function from a admin page'''
    WIN.destroy()
    from dashboard import dashboard
    dashboard()

def homepage():
    WIN = Tk()
    WIN.title('Online Banking System')
    WIN.geometry('360x640')
    background = PhotoImage(file="images/userdashboard.png")
    label_background = Label(WIN,image=background,borderwidth=0)
    label_background.place(x=0,y=0)
    
    
    button_image = PhotoImage(file="images/arrow.png")
    button = Button(WIN, image=button_image, borderwidth=0, width=30, height=30,command = lambda:dashboard_call(WIN))
    button.place(x=4, y=5)


    def add_user_page():
        '''Destroys the tkinter window and call open_login function i.e. login function from a login page'''
        WIN.destroy()
        from adduser import add_new_user
        add_new_user()
        
    def user_list_page():
        '''Destroys the tkinter window and call open_login function i.e. login function from a login page'''
        WIN.destroy()
        from user_list import view_users
        view_users()
    
    def remove_users_page():
        '''Destroys the tkinter window and call open_login function i.e. login function from a login page'''
        WIN.destroy()
        from userdetail import viewusers
        viewusers()


 
    def on_enter_add_user(e):
        add_user.config(background='#7409EB',foreground= "white")


    def on_leave_add_user(e):
        add_user.config(background= '#645394', foreground= 'white')


    add_user = Button(WIN,text="Deposit Money",padx=13,borderwidth=0,font=("Comic Sans MS", 11),background= '#645394', foreground= 'white',command=lambda:add_user_page())
    add_user.place(relx=0.3, rely=0.5, anchor=CENTER)
    add_user.bind('<Enter>',on_enter_add_user)
    add_user.bind('<Leave>',on_leave_add_user)

    def on_enter_remove_users(e):
        remove_users.config(background='#7409EB',foreground= "white")

    def on_leave_remove_users(e):
        remove_users.config(background= '#645394', foreground= 'white')

  
    remove_users= Button(WIN,text="Retrieve Money",padx=13,borderwidth=0,font=("Comic Sans MS", 11),background= '#645394', foreground= 'white',command=lambda:remove_users_page())
    remove_users.place(relx=0.7, rely=0.5, anchor=CENTER)
    remove_users.bind('<Enter>',on_enter_remove_users)
    remove_users.bind('<Leave>',on_leave_remove_users)


    def on_enter_user_list(e):
        '''Changed Background and Foreground of Button named view_voter
        to #edd8ed and white respectively when function is called.'''
        user_list.config(background='#7409EB',foreground= "white")

    def on_leave_user_list(e):
        '''Changed Background and Foreground of Button named view_voter to
        pink and black respectively when function is called.'''
        user_list.config(background= '#645394', foreground= 'white')


    user_list= Button(WIN,text="Request Account Deletion",padx=13,borderwidth=0,font=("Comic Sans MS", 12),background= '#645394', foreground= 'white',command=lambda:user_list_page())
    user_list.place(relx=0.5, rely=0.6, anchor=CENTER)
    user_list.bind('<Enter>',on_enter_user_list)
    user_list.bind('<Leave>',on_leave_user_list)

    def get_total_users():
        return 100

    def homepage():
        total_users = get_total_users()
        total_users_label = Label(WIN,text="Request Account Deletion",padx=13,borderwidth=0,font=("Comic Sans MS", 12),background= '#645394', foreground= 'white',command=lambda:user_list_page())
        total_users_label(relx=0.5, rely=0.6, anchor=CENTER)

    WIN.mainloop()

homepage()