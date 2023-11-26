import socket

server_address = ('localhost', 6962)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect(server_address)
response = client_socket.recv(1024)
print(response.decode())


def client(alphabet_input):
    client_socket.sendall(alphabet_input.encode())

    responser = client_socket.recv(1024)
    print(responser.decode())

    return responser.decode()
