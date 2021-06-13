import socket
import os
from _thread import *
import json
##### function check
def checkExistUsername(user):
    user_str = user['username']
    for i in arr['users']:
        if user_str == i['username']:
            return True # đã tồn tại
    return False # k tồn tại

def checkUserPassword(user):
    for i in arr['users']:
        if user['username'] == i['username'] and user['password'] == i['password']:
            return True # đúng password
    else: return False # sai password

def checkLogin(user):
    if not checkExistUsername(user): 
        return 'Username does not found!'  # k tồn tại username
    elif not checkUserPassword(user): 
        return 'Your password is incorrect!'  # k đúng password
    else: return 'Logged in successfully!'


f = open('./data.json', "r")
arr = json.loads(f.read())
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
            data = connection.recv(2048)
            # reply = 'Server Says: ' + data.decode('utf-8')
            if data.decode('utf-8') == 'login':
                username = connection.recv(2048).decode('utf-8')
                pw = connection.recv(2048).decode('utf-8')
                user = {}
                user['username'] = username
                user['password'] = pw
                respone = checkLogin(user)
                connection.sendall(str.encode(respone))
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
