# import modules

from tkinter import *
import tkinter.messagebox as mbox
import os

global list_of_files
list_of_files = os.listdir("C:")


# Designing window for registration

def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("500x350")

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(register_screen, text="Please enter details below", bg="light blue").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Username  ")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, text="Password  ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=15, height=1, bg="orange", command=register_user).pack()


# Designing window for login

def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("500x350")
    Label(login_screen, text="Please enter details below to login", bg="yellow").pack()
    Label(login_screen, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    Label(login_screen, text="Username  ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password  ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show='*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=15, height=1, command=login_verify).pack()


# Implementing event on register button

def register_user():
    username_info = username.get()
    password_info = password.get()
    if username_info in list_of_files:
        file1 = open(username_info, "r")
        verify = file1.read().splitlines()
        if username_info in verify:
            mbox.showerror("Error!","Username already exists")
            Label(register_screen, text="Unable to register!Check Username/Password", fg="red", font=("calibri", 11)).pack()
            Button(register_screen,text="OK", width=15, height=1, command=register_screen.destroy()).pack()
    else:
        if check_pass(password_info) == 1:

            file = open(username_info, "w")
            file.write(username_info + "\n")
            file.write(password_info)
            file.close()

            username_entry.delete(0, END)
            password_entry.delete(0, END)
            Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()
        else:
            mbox.showerror("Error!","Password requirements not met")
            Label(register_screen, text="Unable to register", fg="red", font=("calibri", 11)).pack()
            register_screen.destroy()


# Password validator
def check_pass(password):
    flag=0
    while True:
        if len(password) < 8:
            flag = -1
            break
        elif not re.search("^[a-zA-Z]", password):
            flag = -1
            break
        elif not re.search("[0-9]", password):
            flag = -1
            break
        elif not re.search("[_@#]", password):
            flag = -1
            break
        else:
            flag = 0
            return 1

    if flag == -1:
        return 0


# Implementing event on login button

def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)


    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()

        if password1 in verify:
            login_sucess()
        else:
            password_not_recognised()

    else:
        user_not_found()


# Designing popup for login success

def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK", command=delete_login_success).pack()


# Designing popup for login invalid password

def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Error!")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Wrong Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()


# Designing popup for user not found

def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("No User!")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()

# Deleting popups

def delete_login_success():
    login_success_screen.destroy()


def delete_password_not_recognised():
    password_not_recog_screen.destroy()


def delete_user_not_found_screen():
    user_not_found_screen.destroy()


# Designing Main(first) window

def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("600x400")
    main_screen.title("Account Login")
    Label(text="Select Your Choice", bg="red", width="300", height="2", font=("Arial", 13)).pack()
    Label(text="").pack()
    Button(text="Login",bg="light green", height="2", width="30", command=login).pack()
    Label(text="").pack()
    Button(text="Register",bg="light green", height="2", width="30", command=register).pack()

    main_screen.mainloop()

main_account_screen()