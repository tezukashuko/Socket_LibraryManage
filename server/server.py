import socket
import os  # getfilesize
import threading
import pickle  # arr to str
import svfunc
import sys
from struct import pack
# function check
#####
ServerSocket = socket.socket()
hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
port = 50327  # 5 + 2 số cuối mssv 03 và 27
# ThreadCount = 0

while True:
    try:
        ServerSocket.bind((local_ip, port))
        break
    except socket.error as e:
        print('Cannot create Server, trying another port')
        port += 1


print('Server IP:port: ' + str(local_ip) + ':' + str(port) + ', please copy to Clients')
print('Waiting for a Connection..')
ServerSocket.listen(5)  # enable server to accept() connection
def threaded_client(connection):
    try:
        while True:
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
                arrbyte = pickle.dumps(search)
                search_length = pack('>Q',sys.getsizeof(arrbyte)) # pack to unsigned long long int 
                connection.sendall(search_length)
                # print(bookarr)
                connection.sendall(arrbyte)
                ack = connection.recv(1)
            elif arr[0] == 'searchheader':
                searchheader = svfunc.getsearcHeader()
                # print(bookarr)
                connection.sendall(pickle.dumps(searchheader))
            # elif arr[0] == 'getfilesize':
            #     address = connection.getpeername()
            #     print(address[0] + ':' + str(address[1]) + ' ==> Getting filesize of ' +
            #           arr[1] + ' from server, preparing for download')
            #     file_size = os.path.getsize('booksv/'+arr[1])
            #     connection.sendall(str(file_size).encode('utf-8'))
            elif arr[0] == 'download':
                address = connection.getpeername()
                print(address[0] + ':' + str(address[1]) + ' ==> Getting filesize of ' +
                      arr[1] + ' from server, preparing for download')

                f = open('./booksv/'+arr[1], 'rb')
                data = f.read()
                file_size = pack('>Q',sys.getsizeof(data)) # pack to unsigned long long int 
                connection.sendall(file_size)

                print(address[0] + ':' + str(address[1]) +
                      ' ==> Started send ' + arr[1] + ' from server')
                connection.sendall(data)
                f.close()
                print(address[0] + ':' + str(address[1]) +' ==> Sent ' + arr[1] + ' completely to client')
                ack = connection.recv(1)

        connection.close()
    except:  # if client auto out
        address = connection.getpeername()
        print(address[0] + ':' + str(address[1]) + ' has been disconnected')
        connection.close()
while True:
    Client, address = ServerSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    threading._start_new_thread(threaded_client, (Client, ))
ServerSocket.close()
