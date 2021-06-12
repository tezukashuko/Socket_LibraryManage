import socket



from tkinter import *
import time



root = Tk()



root.title("Library Manage")





####### socket connection ######



ClientSocket = socket.socket()



host = '127.0.0.1'



port = 1233



waiting = Label(root, text='Connecting to server')



waiting.pack(pady=5)



try:


    ClientSocket.connect((host, port))



except socket.error as e:


    Label(root, text='Cannot connect to server').pack(pady=5)
    root.mainloop()



waiting.destroy()



Label(root, text='Connected to server').pack(pady=5)



####### socket connection ######



############## Login frame ####################



login_frm = LabelFrame(root, text='Login')


login_frm.pack(fill='x', padx=10, pady=5)



username_lbl = Label(login_frm, text="Username")



username_lbl.grid()



username_inp = Entry(login_frm)



username_inp.grid(row=0, column=2)



pw_lbl = Label(login_frm, text="Password")



pw_lbl.grid()



pw_inp = Entry(login_frm)



pw_inp.grid(row=1, column=2)



def login():
    str = username_inp.get()


    if (str == ''):
        print(str)


        username_inp.delete(0, 'end')


        pw_inp.delete(0, 'end')


        success.configure(text='success')


        # add check in here

        login_frm.pack_forget()


        success.pack(pady=5)


        Logout_btn.pack(pady=5)


        search_frm.pack(pady=5, padx=5, fill='x')


    else:


        errorusername.configure(text='username error')



login_btn = Button(login_frm, text="Login",




                   fg="red", command=login)



# set Button grid



login_btn.grid(row=2, column=2, sticky='w')



reg_btn = Button(login_frm, text="Register",






                 fg="red", command=login)



# set Button grid



reg_btn.grid(row=2, column=2, sticky='e', pady=5)



errorusername = Label(login_frm, text='', fg='red')



errorusername.grid(row=0, column=3, pady=5)



errorpw = Label(login_frm, text='', fg='red')



errorpw.grid(row=1, column=3)



############## end Login frame ####################



success = Label(root, text='login success', fg='red')



print(success.cget('text'))



def logout():


    login_frm.pack(fill='x',padx=10, pady=5)


    Logout_btn.pack_forget()


    success.pack_forget()


    search_frm.pack_forget()



Logout_btn = Button(root, text="Logout",



                    fg="red", command=logout)


###### search frame ##########

search_frm = LabelFrame(root, text='Search')


#####

search_info = Frame(search_frm)

search_info.pack(pady=5, padx=5, fill='x')

searchrule = ['F_ID: ID là mã sách. VD: F_ID 1234', 'F_Name : Name là tên sách. VD: F_Name "Computer Networking"',

              'F_Type: Type là loại sách. VD: F_Type "Computer Science"', 'F_Author: Author là tên tác giả. VD: F_Author "Jack London"']

for x in searchrule:

    Label(search_info, text=x).grid(sticky='w')
#####

#####
search_inp_frm = Frame(search_frm)
search_inp_frm.pack(fill='x', padx=5, pady=5)


search_lbl = Label(search_inp_frm, text="Type here: ")

search_lbl.grid(sticky='w')

search_inp = Entry(search_inp_frm)

search_inp.grid(row=0, column=2)



def search():
    str = search_inp.get()
    errorsearch.configure(text = 'search error')
    if (search_res_frm.winfo_exists()):
        for widgets in search_res_frm.winfo_children():
            widgets.destroy()
    search_res_frm.pack(fill = 'x', padx = 10, pady = 10)
    
    Label(search_inp_frm, text = str).grid()


search_btn = Button(search_inp_frm, text='Search', command=search)

search_btn.grid(row=0, column=3, padx=5)

errorsearch = Label(search_inp_frm, text='', fg='red')

errorsearch.grid(column = 2)
######

###### result frame ##########
search_res_frm = Frame(search_frm)
search_res_frm.pack(fill = 'x', padx = 10, pady = 10)
Label(search_res_frm,text = 'asd').grid()   


###### result frame ##########


###### search frame ##########
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

