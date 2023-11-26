import socket
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
server_address = ('localhost', 6969)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(server_address)
server_socket.listen(1)
print(f"Server listening on {server_address[0]}:{server_address[1]}")
client_socket, client_address = server_socket.accept()
client_socket.sendall("Start your alphabet\n".encode())
direction = 1
place = 0
score = 0
try:
    while True:
        current_letter = ALPHABET[place]
        data = client_socket.recv(4)
        data = data.decode()
        if data[0].lower() != current_letter:
            client_socket.sendall(f"Incorrect, the correct letter was {current_letter}\n"
                                  f"Your score is: {score}\n"
                                  f"Thanks for playing!\n".encode())
            break
        score += 1
        place += direction
        if place < 0:
            place = 1
            client_socket.sendall(f"You have reached the start, now go forwards.\n".encode())
            direction = 1
        elif place > 25:
            place = 24
            client_socket.sendall(f"You have reached the end, now go backwards.\n".encode())
            direction = -1
    client_socket.sendall("Goodbye.\n".encode())
finally:
    client_socket.close()
