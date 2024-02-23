from tkinter import *
from tkinter import messagebox  # Corrected import
from cryptography.fernet import Fernet
from stegano import lsb
import json

# Function to decrypt a message using the provided key
def decrypt_message(encrypted_message, key):
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message.encode())  # Ensure encrypted_message is in bytes
    return decrypted_message

def userlogin_data_error():
    # Display an error message box
    messagebox.showerror("Login Error", "Invalid phone number or PIN.")

def userlogin_validation(WIN, phonenumber, entered_pin, key):
    image_path = "images/img.png"
    try:
        decoded_data = lsb.reveal(image_path)
        if not decoded_data:
            print("No data found in the image.")
            return False
        
        user_data = json.loads(decoded_data)

        for i in user_data["users"]:
            if i[2] == phonenumber:  # Assuming index 2 is the phone number
                encrypted_pin =  str(i[7])  # Assuming index 7 is the encrypted PIN
                decrypted_pin = decrypt_message(encrypted_pin, key)  # Pass the key to decrypt
                if decrypted_pin == entered_pin:
                    print("User Login Success")
                    WIN.destroy()
                    # Load the user dashboard or next steps here
                    return True
        print("User Login Failed - Incorrect phone number or PIN.")
    except Exception as e:
        print(f"Error during login validation: {e}")
    
    userlogin_data_error()
    return False

def userlogin():
    WIN = Tk()
    WIN.title('Online Banking System')
    WIN.geometry('360x640')

    # Load the encryption key (ensure it's the same key used for encryption)
    key = b'your_encryption_key_here'  # Use the actual key you saved during encryption

    background = PhotoImage(file="images/userlogin.png")
    label_background = Label(WIN, image=background, borderwidth=0)
    label_background.place(x=0, y=0)
    w = Canvas(WIN, width=350, height=280, borderwidth=0, highlightthickness=0)
    w.create_rectangle(0, 0, 350, 300, fill="#FFFFFF", outline='#000000')
    w.pack(padx=40, pady=(310,0))
   
    def temp_user_id(e):
        user_id_entry.delete(0, "end")

    user_id_entry = Entry(WIN, font=("Comic Sans MS", 14), justify="center", width=15, foreground="#AFAFAF")
    user_id_entry.insert(2, "Mobile Number")
    user_id_entry.bind("<FocusIn>", temp_user_id)
    user_id_entry.place(relx=0.5, rely=0.6, anchor=CENTER)

    def temp_password(e):
        password_entry.config(show="*")
        password_entry.delete(0, "end")

    password_entry = Entry(WIN, font=("Comic Sans MS", 14), justify="center", width=15, foreground="#AFAFAF")
    password_entry.insert(0, "Password")
    password_entry.bind("<FocusIn>", temp_password)
    password_entry.place(relx=0.5, rely=0.7, anchor=CENTER)

    userlogin_button = Button(WIN, font=("Comic Sans MS", 14), justify="center", width=10, borderwidth=0, text="Log In", bg="#645394", command=lambda: userlogin_validation(WIN, user_id_entry.get(), password_entry.get(), key))
    userlogin_button.place(relx=0.5, rely=0.8, anchor=CENTER)

    WIN.mainloop()

userlogin()
