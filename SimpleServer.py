import socketserver

# Define initial states
devices = {
    'FR': 'OFF',
    'K': 'OFF',
    'T': 70
}

class SDCPRequestHandler(socketserver.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024).strip()
        print(f"Received {self.data} from {self.client_address[0]}")

        message = self.data.decode().split()

        if message[0] == 'STATUS':
            if message[1] == 'ALL':
                response = '\n'.join([f"{device} {state}" for device, state in devices.items()])
            else:
                response = f"{message[1]} {devices.get(message[1], 'UNKNOWN')}"
        elif message[0] == 'SET':
            devices[message[1]] = message[2]
            response = f"{message[1]} set to {message[2]}"
        else:
            response = "INVALID COMMAND"

        self.request.sendall(response.encode())

if __name__ == "__main__":
    HOST, PORT = '10.0.0.1', 4488
    server = socketserver.TCPServer((HOST, PORT), SDCPRequestHandler)
    print(f"Server running on {HOST}:{PORT}")
    server.serve_forever()
