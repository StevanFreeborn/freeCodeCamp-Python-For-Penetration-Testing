import socket

client_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

host = socket.gethostname()

port = 444

client_socket.connect((host, port))

message = client_socket.recv(1024)

client_socket.close()

print(message.decode('ascii'))