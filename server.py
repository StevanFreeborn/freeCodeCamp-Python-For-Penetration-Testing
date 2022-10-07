import socket

server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

host = socket.gethostname()
port = 444

server_socket.bind((host, port))

server_socket.listen()

while True:
    client_socket, address = server_socket.accept()
    print(f'received connection from {address}')
    message = f'Hello! Thank you for connecting to the server.\r\n'
    client_socket.send(message)
    client_socket.close()