import socket
import pickle 


def savefile(infosocket,name):

    ClientSocket = socket.socket()
    ClientSocket.connect((infosocket[0], infosocket[1]))
    arr = ['download', name]

    ClientSocket.sendall(pickle.dumps(arr))
    file = open('./bookdownload/'+name,'wb')
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