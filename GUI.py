
from tkinter import *
import time
root = Tk()


root.title("Library Manage")


####### socket connection ######
import socket

ClientSocket = socket.socket()
host = '127.0.0.1'
port = 1233

print('Waiting for connection')
try:
    ClientSocket.connect((host, port))
except socket.error as e:
    Label(root, text='Cannot connect to server').grid(sticky='n')
    root.mainloop()
    


    

Label(root, text='Connected to server').grid(padx=5, pady=5, sticky='n')
    



####### socket connection ######

############## Login frame ####################

frame = LabelFrame(root, text='Login')
frame.grid(padx=10, pady=10, columnspan=3, sticky='ew')


username_lbl = Label(frame, text="Username")


username_lbl.grid()


username_inp = Entry(frame)


username_inp.grid(row=0, column=2)


pw_lbl = Label(frame, text="Password")


pw_lbl.grid()


pw_inp = Entry(frame)


pw_inp.grid(row=1, column=2)


def login():

    frame.grid_forget()

    str = username_inp.get()

    if (str == 'login'):
        print(str)

        success.configure(text='success')

    else:

        errorusername.configure(text='username error')


login_btn = Button(frame, text="Login",
                   fg="red", command=login)


# set Button grid

login_btn.grid(row=2, column=2, sticky='w')


reg_btn = Button(frame, text="Register",


                 fg="red", command=login)


# set Button grid

reg_btn.grid(row=2, column=2, sticky='e', pady=5)


errorusername = Label(frame, text='', fg='red')


errorusername.grid(row=0, column=3, pady=5)


errorpw = Label(frame, text='', fg='red')


errorpw.grid(row=1, column=3)


success = Label(frame, text='success', fg='red')


success.grid(row=3, column=2)

print(success.cget('text'))


############## end Login frame ####################
def login():
    frame.grid()

    # str = username_inp.get()

    # if (str == 'login'):
    #     print(str)

    #     success.configure(text='success')

    # else:

    #     errorusername.configure(text='username error')


Logout_btn = Button(root, text="Logout",


                    fg="red", command=login)

Logout_btn.grid()
root.mainloop()

# ClientSocket.close()


# def senddata(str):
#     if(str == ''):
#         return


# username = tk.Entry(
# )

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
