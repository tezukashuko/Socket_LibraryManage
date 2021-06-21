import socket

import os  # getfilesize

from _thread import *

import pickle  # arr to str

import svfunc


# function check


#####

<<<<<<< Updated upstream
ServerSocket = socket.socket() # create a socket object
host = '127.0.0.1'
port = 1233
=======

ServerSocket = socket.socket()

hostname = socket.gethostname()

local_ip = socket.gethostbyname(hostname)

port = 50327  # 5 + 2 số cuối mssv 03 và 27

>>>>>>> Stashed changes
ThreadCount = 0


try:
<<<<<<< Updated upstream
    ServerSocket.bind((host, port)) # associate the socket with a specific network interface and port number
=======

    ServerSocket.bind((local_ip, port))
>>>>>>> Stashed changes
except socket.error as e:
    print('Cannot create Server')

print('Server IP:host: ' + str(local_ip) + ':' + str(port)+ ', please type it to connect in Client'
      )
print('Waiting for a Connection..')
ServerSocket.listen(5) # enable server to accept() connection


def threaded_client(connection):

    try:

        while True:
<<<<<<< Updated upstream
            data = connection.recv(1024) #  reads whatever data the client sends
=======

            data = connection.recv(1024)

>>>>>>> Stashed changes
            # print('recved')

            arr = pickle.loads(data)
            # print(arr)

            # reply = 'Server Says: ' + data.decode('utf-8')

            if arr[0] == 'login':

                user = {}

                user['username'] = arr[1]

                user['password'] = arr[2]

                respone = svfunc.checkLogin(user)
<<<<<<< Updated upstream
                print(respone)
                connection.sendall(respone.encode('utf-8')) # echo back respone to client
=======
                # print(respone)

                connection.sendall(respone.encode('utf-8'))
>>>>>>> Stashed changes

            elif arr[0] == 'register':

                user = {}

                user['username'] = arr[1]

                user['password'] = arr[2]

                respone = svfunc.createNewUser(user)
                # print(str(respone))

                connection.sendall(str(respone).encode('utf-8'))

            elif arr[0] == 'search':

                search_str = arr[1]

                bookarr = svfunc.searchBook(search_str)

                # print(bookarr)

                connection.sendall(pickle.dumps(bookarr))

            elif arr[0] == 'getfilesize':
                address = connection.getpeername()
                print(address[0] + ':' + str(address[1]) + ' ==> Getting filesize of ' + arr[1]+ ' from server, preparing for download')

                file_size = os.path.getsize('./booksv/'+arr[1])

                connection.sendall(str(file_size).encode('utf-8'))

            elif arr[0] == 'download':
                address = connection.getpeername()
                print(address[0] + ':' + str(address[1]) + ' ==> Started download ' + arr[1]+ ' from server')
                f = open('./booksv/'+arr[1], 'rb')

                data = f.read(1024)

                while data:
                    connection.send(data)

                    data = f.read(1024)

                    if not data:
                        print(address[0] + ':' + str(address[1]) + ' ==> Sent ' + arr[1]+ ' completely to client')
                        break

                # connection.sendall(respone.encode('utf-8'))

            # if not data:

            #     break

            # connection.sendall(str.encode(reply))
        connection.close()

    except:  # if client auto out

        address = connection.getpeername()

        print(address[0] + ':' + str(address[1]) + ' has been disconnected')


while True:

    Client, address = ServerSocket.accept()

    print('Connected to: ' + address[0] + ':' + str(address[1]))

    start_new_thread(threaded_client, (Client, ))

    ThreadCount += 1

    print('Thread Number: ' + str(ThreadCount))

ServerSocket.close()
