import socket
import os
from _thread import *
import pickle
import func
##### function check
arr = func.arr
#####



ServerSocket = socket.socket()
host = '127.0.0.1'
port = 1233
ThreadCount = 0
try:
    ServerSocket.bind((host, port))
except socket.error as e:
    print(str(e))

print('Waiting for a Connection..')
ServerSocket.listen(5)


def threaded_client(connection):
    try:
        while True:
            data = connection.recv(1024)
            print('recved')
            arr = pickle.loads(data)
            print(arr)
            # reply = 'Server Says: ' + data.decode('utf-8')
            if arr[0] == 'login':
                print(arr[1])
                print(arr[2])
                user = {}
                user['username'] = arr[1]
                user['password'] = arr[2]
                respone = func.checkLogin(user)
                print(respone)
                connection.sendall(respone.encode('utf-8'))
            elif arr[0] == 'search':
                search_str = arr[1]
                book = func.searchBook(search_str)
                print(book)
                #connection.sendall(respone.encode('utf-8'))
            # if not data:
            #     break
            # connection.sendall(str.encode(reply))
        connection.close()
    except: ##if client auto out
        address = connection.getpeername()
        print(address[0] + ':' + str(address[1]) +  ' has been corrupted')


while True:
    Client, address = ServerSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(threaded_client, (Client, ))
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))
ServerSocket.close()
