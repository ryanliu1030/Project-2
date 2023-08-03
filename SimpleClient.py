import socket

HOST, PORT = '10.0.0.1', 4488

while True:
    command = input('Enter command: ')
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((HOST, PORT))
        sock.sendall(command.encode())
        response = sock.recv(1024)
        print("Received: ", response.decode())
