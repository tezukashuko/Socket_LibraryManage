import socket
import os  # getfilesize
import threading
import pickle  # arr to str
import svfunc
from struct import pack
from tkinter import *
from tkinter import messagebox
# function check
#####
ServerSocket = socket.socket()
hostname = socket.gethostname()
host = socket.gethostbyname(hostname)
port = 50327
# ThreadCount = 0
while True:
    try:
        ServerSocket.bind((host, port))
        break
    except socket.error as e:
        port += 1

serverip = ServerSocket.getsockname()
serverIP_str = serverip[0] + ':'+str(serverip[1])
notiIP = "Server IP:port: " + serverIP_str + ", please copy to Clients"
ServerSocket.listen(5)
def threaded_client(connection):
    try:
        # reads whatever data the client sends
        data = connection.recv(1024)
        # print('recved')
        arr = pickle.loads(data)
        # print(arr)
        # reply = 'Server Says: ' + data.decode('utf-8')
        if arr[0] == 'login':
            user = {}
            user['username'] = arr[1]
            user['password'] = arr[2]
            respone = svfunc.checkLogin(user)
            # print(respone)
            connection.sendall(respone.encode('utf-8'))
        elif arr[0] == 'register':
            user = {}
            user['username'] = arr[1]
            user['password'] = arr[2]
            respone = svfunc.createNewUser(user)
            # print(str(respone))
            connection.sendall(str(respone).encode('utf-8'))
        elif arr[0] == 'search':
            search_str = arr[1]
            search = svfunc.searchBook(search_str)
            # print(bookarr)
            connection.sendall(pickle.dumps(search))
        elif arr[0] == 'searchheader':
            searchheader = svfunc.getsearcHeader()
            # print(bookarr)
            connection.sendall(pickle.dumps(searchheader))
        elif arr[0] == 'getfilesize':
            address = connection.getpeername()
            print(address[0] + ':' + str(address[1]) + ' ==> Getting filesize of ' +
                    arr[1] + ' from server, preparing for download')
            file_size = os.path.getsize('./booksv/'+arr[1])
            connection.sendall(str(file_size).encode('utf-8'))
        elif arr[0] == 'download':
            address = connection.getpeername()
            print(address[0] + ':' + str(address[1]) +
                    ' ==> Started download ' + arr[1] + ' from server')
            file_size = os.path.getsize('./booksv/'+arr[1])
            f = open('./booksv/'+arr[1], 'rb')
            while True:
                data = f.read(1024)
                connection.sendall(data)
                file_size -= 1024
                if file_size <= 0:
                    f.close()
                    print(address[0] + ':' + str(address[1]) +
                            ' ==> Sent ' + arr[1] + ' completely to client')
                    break
        threaded_client(connection)
    except:  # if client auto out
        global scrollable_frame
        address = connection.getpeername()
        status = address[0] + ':' + str(address[1]) + ' has been disconnected'
        Label(scrollable_frame, text=status).grid()
        connection.close()
        connectClient()
def connectClient():
    # global ThreadCount
    Client, address = ServerSocket.accept()
    clientstr = 'Connected to: ' + address[0] + ':' + str(address[1])
    Label(scrollable_frame, text=clientstr).grid()
    threading._start_new_thread(threaded_client, (Client, ))
    root.after(1000, connectClient)
def createScrollFrame(frame):
    canvas = Canvas(frame)
    scrollable_frame = Frame(canvas)
    ScrollBarH = Scrollbar(frame)
    ScrollBarV = Scrollbar(frame)
    canvas.config(xscrollcommand=ScrollBarH.set,
                  yscrollcommand=ScrollBarV.set, highlightthickness=0, height=500)
    ScrollBarH.config(orient=HORIZONTAL, command=canvas.xview)
    ScrollBarV.config(orient=VERTICAL, command=canvas.yview)
    ScrollBarH.pack(fill=X, side=BOTTOM, expand=FALSE)
    ScrollBarV.pack(fill=Y, side=RIGHT, expand=FALSE)
    canvas.pack(fill=BOTH, side=LEFT, expand=TRUE)
    canvas.create_window(0, 0, window=scrollable_frame, anchor=NW)
    return canvas, scrollable_frame
root = Tk()
root.title("Library Manage - Server")
Label(root, text=notiIP).pack()  # hiện ip cho ng dùng nhập
server_frm = Frame(root)
server_frm.pack(fill='x', padx=10, pady=10)
canvas, scrollable_frame = createScrollFrame(server_frm)
root.after(1000, connectClient)
root.mainloop()
ServerSocket.close()
