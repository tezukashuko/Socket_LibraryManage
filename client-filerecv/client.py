import socket

ClientSocket = socket.socket()
host = '127.0.0.1'
port = 1233

print('Waiting for connection')
try:
    ClientSocket.connect((host, port))
except socket.error as e:
    print(str(e))
file = open('rev.pdf','wb')

Response = ClientSocket.recv(1024)

while Response:
    file.write(Response)
    Response = ClientSocket.recv(1024)
# while True:
#     Input = input('Say Something: ')
#     if Input == '' :
#         break
#     ClientSocket.send(str.encode(Input))
#     Response = ClientSocket.recv(1024)
#     print(Response.decode('utf-8'))

ClientSocket.close()
