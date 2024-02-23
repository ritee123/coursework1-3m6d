#Imported Necessary Modules
from tkinter import *
from tkinter import ttk
import ast
from PIL import Image
from stegano import lsb
import json


def data_not_found():

    title = "Username Not Found"
    message = "Input Username was\n not Found"
    from errors import error as show_error
    show_error(title, message)
    
def return_adminhomepage(WIN):
    WIN.destroy()
    from admin_dashboard import homepage
    homepage()


def view_users():
    WIN_viewvuser = Tk()
    WIN_viewvuser.title('Online Banking System')
    WIN_viewvuser.geometry('360x640')

    background = PhotoImage(file="images/current user.png")
    label_background = Label(WIN_viewvuser, image=background, borderwidth=0)
    label_background.place(x=0, y=0)
    w = Canvas(WIN_viewvuser, width=320, height=430, borderwidth=0, highlightthickness=0)
    w.create_rectangle(0, 0, 320, 600, fill="#645394", outline='#edd09f')
    w.pack(padx=(20), pady=(190,0))

    tv = ttk.Treeview(WIN_viewvuser, show='tree', height=9)
    ttk.Style().theme_use("default")
    ttk.Style().configure("Treeview", background="#645394",foreground="white",fieldbackground="#645394", rowheight=31,font = ("Comic Sans MS", 12), highlightthickness=0, bd=0,padding=10,columns=1)
    ttk.Style().map("Treeview",background=[('selected','#645394')],foreground=[('selected','white')])
    tv['columns']=('Name', 'Age')
    tv.column('#0', width=0, stretch=NO)
    tv.column('Name', anchor=W, width=140)
    tv.column('Age', anchor=E, width=98)      
    
    # Function named Search
    def search():
        try:
            for value in orginal_userlist:
                if username_search.get() == value[0]:
                    for item in tv.get_children():
                        tv.delete(item)
                    tv.insert(parent='', index=1, iid=1, text='', values=value)
                    break
                elif username_search.get() == "":
                    for item in tv.get_children():
                        tv.delete(item)
                    b = 1
                    for data in userlist:
                        tv.insert(parent='', index=b, iid=b, text='', values=data)
                        b = b + 1
                    break
            else:
                raise ValueError('Value Not found')
        except:
            data_not_found()

   
    def reback():
        WIN_viewvuser.destroy()
        from admin_dashboard import homepage
        homepage()

    username_search = Entry(WIN_viewvuser, font=("Comic Sans MS", 11), justify="center", width=15, foreground="#AFAFAF")
    username_search.place(relx=0.4, rely=0.4, anchor=CENTER)

    def temp_username(e):
        '''Clears phone_entry to take user input'''
        username_search.delete(0, "end")
    username_search.bind("<FocusIn>",temp_username)
    username_search.insert(1,"Enter User Name")
    search_button = Button(WIN_viewvuser, text="Search", padx=9, borderwidth=0, font=("Comic Sans MS", 9),width=6, background='#d98d0b', foreground='black', command=search)
    search_button.place(relx=0.7, rely=0.4, anchor=CENTER)
    
    image_path = "images/img.png"
    decoded_data = lsb.reveal(image_path)
    decoded_data = json.loads(decoded_data)

    detailedlist = decoded_data['users']

    userlist = []
    for user in reversed(detailedlist):
        name = (user[0], user[1])
        userlist.append(name)

    orginal_userlist = userlist.copy()
    orginal_length = len(userlist)
    if orginal_length > 7:
        new_length = orginal_length - 7
        for i in range(new_length):
            userlist.pop()

    a = 0
    for data in userlist:
        tv.insert(parent='', index=a, iid=a, text='', values=data)
        a = a + 1
    tv.place(relx=0.5, rely=0.7, anchor=CENTER)
    
    return_image = PhotoImage(file="images/arrow.png")
    return_button = Button(WIN_viewvuser, image=return_image, borderwidth=0, command=lambda: return_adminhomepage(WIN_viewvuser))
    return_button.image = return_image
    return_button.place(x=4, y=5)

    WIN_viewvuser.mainloop()

view_users()