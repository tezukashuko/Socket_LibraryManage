import socket

# HOST = socket.gethostbyname(socket.gethostname())  # Standard loopback interface address (localhost)
HOST = '127.0.0.1'
PORT = 65431        # Port to listen on (non-privileged ports are > 1023)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
# print(f'Created a server with IP: {HOST}, send it to your client')
print("Waiting for connection")
s.listen(2)
# count = 0
while True:
    conn, addr = s.accept()
    # count += 1
    # try:
    #     print('Connected by', addr)
    #     while True:
    #         data = conn.recv(1024)
    #         str_data = data.decode("utf8")
    #         if str_data == "quit" or str_data == 'exit':
    #             break
    #         print("Client: " + str_data)
    #         # Server send input
    #         msg = input("Server: ")
    #         conn.sendall(bytes(msg, "utf8"))
    # finally:
    #     # Clean up the connection
    #     conn.close()
    #     # if count == 2: 
    #     #     break
    #     s.close()