
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server_address = (HOST, PORT)
# print('connecting to port {PORT}' + str(server_address))
# s.connect(server_address)


# try:
#     while True:
#         msg = input('Client: ')
#         s.sendall(bytes(msg, "utf8"))

#         if msg == "quit":
#             break

#         data = s.recv(1024)
#         print('Server: ', data.decode("utf8"))
# finally:
#     print('closing socket')
#     s.close()
