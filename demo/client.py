import socket

HOST = ""  # The server's hostname or IP address
PORT = 65431        # The port used by the server
# Create a TCP/IP socket
while(True):
    print(f'Your server IP is {socket.gethostbyname(socket.gethostname())}')
    confirm = input("Type y(yes) or n(No): ")
    if confirm == 'y':
        HOST = socket.gethostbyname(socket.gethostname())
        break
    else:
        confirm = input("your IP server: ")
        HOST = confirm


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (HOST, PORT)
s.connect(server_address)
print('connected to port {PORT}' + str(server_address))


try:
    while True:
        msg = input('Client: ')
        s.sendall(bytes(msg, "utf8"))

        data = s.recv(1024)

        if msg == "quit" or msg == "exit":
            break

        print('Server: ', data.decode("utf8"))


finally:
    print('closing socket')
    s.close()
