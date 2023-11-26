import socket
server_address = ('localhost', 6969)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(server_address)
server_socket.listen(1)
print(f"Server listening on {server_address[0]}:{server_address[1]}")
client_socket, client_address = server_socket.accept()
client_socket.sendall("Start your alphabet\n".encode())
try:
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        data = client_socket.recv(4)
        data = data.decode()
        if data[0].lower() != letter:
            client_socket.sendall("incorrect!n".encode())
            break
    client_socket.sendall("goodbye\n".encode())
finally:
    client_socket.close()
