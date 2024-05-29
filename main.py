import socket
#  first create a tcp server and listen for incoming connections
def start_server(host="127.0.0.1", port=6379):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    
    server.bind((host, port))
    server.listen(5) 
    print(f"Server started listening on {host}:{port}")
    
    while True:
        client, addr = server.accept()
        print(f"Connection from {addr}")
        data = client.recv(1024)
        print(f"Received: {data.decode()}")
        client.sendall(b"Hello from server")
        client.close()

if __name__ == "__main__":
    try:
        start_server()
    except KeyboardInterrupt:
        print("Server shut down")