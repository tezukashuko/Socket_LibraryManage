

from tkinter import *


root = Tk()



root.title("Library Manage")

root.geometry('350x200')


username_lbl = Label(root, text="Username")

username_lbl.grid()


username_inp = Entry(root)

username_inp.grid(row=0, column=2)



pw_lbl = Label(root, text="Password")

pw_lbl.grid()


pw_inp = Entry(root)

pw_inp.grid(row=1, column=2)



def clicked():

    str = username_inp.get()

    if (str == 'login'):
        print(str)
        success.configure(text='success')
    else:

        error.configure(text='username eor')


login_btn = Button(root, text="Login",

             fg="red", command=clicked)

# set Button grid
login_btn.grid(row=2,column = 2)



errorusername = Label(root, text='', fg='red')

errorusername.grid(row=1, column=3)


errorpw = Label(root, text='', fg='red')

errorpw.grid(row=2, column=3)


success = Label(root, text='', fg='red')

success.grid(row=3, column=2)


# Execute Tkinter
root.mainloop()

#####################################
# import tkinter as tk


# window = tk.Tk()

# window.title('Library Manage')

# window.geometry('350x200')


# usernamelabel = tk.Label(

#     text='Username'
# )

# username = tk.Entry(
# )
# usernamelabel.pack()
# username.pack()


# def login():
#     global username
#     user = username.get()

#     label = tk.Label(

#         text=user
#     )
#     label.pack()


# btnlogin = tk.Button(

#     text='login',
#     command=login
# )


# btnregister = tk.Button(

#     text='Res'
# )
# btnlogin.pack()
# btnregister.pack()



# lbl = tk.Label(window, text="Hello")

# lbl.grid(column=0, row=0)

# window.mainloop()

