import socket


host = "localhost"
port = 3000


data = "Hello, world!"

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((host, port))


client_socket.send(data.encode())


client_socket.close()
