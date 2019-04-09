import socket

s = socket.socket()
s.bind(("localhost", 8080))

s.listen(1)


while True:
    new_socket, address_information = s.accept()
    # print(new_socket)
    # print(address_information)

    # new_socket.send(b"hello world!")
    message = new_socket.recv(1111)
    print(message)
    new_socket.sendall(b"hello world")
    # new_socket.close()




