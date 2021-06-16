import socket

from tkinter import *
import time

import pickle #convert list to string




def CntToServer(host, port):



    try:



        ClientSocket.connect((host, port))



        return 'Connected'



    except socket.error as e:



        return 'Cannot connect to server'




root = Tk()




root.title("Library Manage")




####### socket connection ######




ClientSocket = socket.socket()




connect_frm = LabelFrame(root, text='Connect to server')



connect_frm.pack(pady=5, padx=5, fill='x')




Label(connect_frm, text='Type your server IP:host, ex: 127.0.0.1:1233').pack()



ip_inp = Entry(connect_frm)



ip_inp.insert('0', '127.0.0.1:1233')



ip_inp.pack()




def connect():



    try:
        str = ip_inp.get()



        arr = str.split(':')



        host = arr[0]



        port = int(arr[1])



        waiting.configure(text='Connecting to server')



        time.sleep(1)



        respone = CntToServer(host, port)



        if respone == 'Connected':



            connect_frm.pack_forget()



            connect_status.configure(text=respone + ' to server')



            login_frm.pack(fill='x')
            print(respone)



        elif respone == 'Cannot connect to server':



            waiting.configure(text=respone)



            waiting.pack()



    except:



        waiting.configure(text='Invalid IP:host')



        waiting.pack()




connect_btn = Button(connect_frm, text='Connect', fg='red', command=connect)



connect_btn.pack(pady=5, padx=5)



waiting = Label(connect_frm, text='', fg='red')



####### socket connection ######




############## Login frame ####################


login_frm = Frame(root)


connect_status = Label(login_frm, text='', fg='red')


connect_status.pack(pady=5)



login_lbl_frm = LabelFrame(login_frm, text='Login')


login_lbl_frm.pack(fill='x', padx=5, pady=5)



username_lbl = Label(login_lbl_frm, text="Username")


username_lbl.grid()



username_inp = Entry(login_lbl_frm)


username_inp.insert(0, 'admin')


username_inp.grid(row=0, column=2)



pw_lbl = Label(login_lbl_frm, text="Password")


pw_lbl.grid()



pw_inp = Entry(login_lbl_frm, show='*')


pw_inp.insert(0, 'admin')


pw_inp.grid(row=1, column=2)




def login():

    errorusername.configure(text = '')

    errorpw.configure(text = '')

    username = username_inp.get()

    pw = pw_inp.get()

    arr = ['login', username, pw]

    ClientSocket.sendall(pickle.dumps(arr))

    # ClientSocket.sendall('login'.encode('utf-8'))

    # ClientSocket.sendall(username.encode('utf-8'))

    # ClientSocket.sendall(pw.encode('utf-8'))

    respone = ClientSocket.recv(1024).decode('utf-8')
    print(respone)

    if (respone == 'Logged in successfully!'):

        username_inp.delete(0, 'end')

        pw_inp.delete(0, 'end')

        success.configure(text=respone)

        # add check in here

        login_frm.pack_forget()

        success.pack(pady=5)

        Logout_btn.pack(pady=5)

        search_frm.pack(pady=5, padx=5, fill='x')



    elif respone == 'Username does not found!':

        errorusername.configure(text = respone)

    elif respone == 'Your password is incorrect!':

        errorpw.configure(text = respone)




login_btn = Button(login_lbl_frm, text="Login", fg="red", command=login)




# set Button grid




login_btn.grid(row=2, column=2, sticky='w')




reg_btn = Button(login_lbl_frm, text="Register", fg="red", command=login)




# set Button grid




reg_btn.grid(row=2, column=2, sticky='e', pady=5)




errorusername = Label(login_lbl_frm, text='', fg='red')




errorusername.grid(row=0, column=3, pady=5)




errorpw = Label(login_lbl_frm, text='', fg='red')




errorpw.grid(row=1, column=3)




############## end Login frame ####################




success = Label(root, text='login success', fg='red')




print(success.cget('text'))




def logout():



    login_frm.pack(fill='x', padx=10, pady=5)



    Logout_btn.pack_forget()



    success.pack_forget()



    search_frm.pack_forget()

Logout_btn = Button(root, text="Logout", fg="red", command=logout)
###### search frame ##########




search_frm = LabelFrame(root, text='Search')


#####




search_info = Frame(search_frm)




search_info.pack(pady=5, padx=5, fill='x')




searchrule = ['Cách search:','F_ID: ID là mã sách. VD: F_ID 1234', 'F_Name : Name là tên sách. VD: F_Name "Computer Networking"',




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
    search = search_inp.get()
    arr = ['search', search]

    errorsearch.configure(text='search error')

    ClientSocket.sendall(pickle.dumps(arr))

    if (search_res_frm.winfo_exists()):



        for widgets in search_res_frm.winfo_children():



            widgets.destroy()



    search_res_frm.pack(fill='x', padx=10, pady=10)



    Label(search_inp_frm, text=search).grid()



search_btn = Button(search_inp_frm, text='Search', command=search)




search_btn.grid(row=0, column=3, padx=5)




errorsearch = Label(search_inp_frm, text='', fg='red')




errorsearch.grid(column=2)
######

###### result frame ##########



search_res_frm = Frame(search_frm)



search_res_frm.pack(fill='x', padx=10, pady=10)



Label(search_res_frm, text='asd').grid()


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


