import socket
import threading
from Redis import MiniRedis

#  first create a tcp server and listen for incoming connections
def start_server(host="127.0.0.1", port=6379):
    redis_instance = MiniRedis()
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    
    server.bind((host, port))
    server.listen(5) 
    print(f"Server started listening on {host}:{port}")
    
    while True:
        client, addr = server.accept()
        print(f"Connection from {addr}")
        clientHandler = threading.Thread(target=handle_client, args=(client, redis_instance))
        clientHandler.start()

def handle_client(clientSocket, redis_instance):
    with clientSocket:
        while True:
            data = clientSocket.recv(1024).decode().strip()
            if not data:
                break
            print(f"Received: {data}")
            data = data.split()
            command = data[0].upper() # first word is always the command
            response = process_command(command, data, redis_instance)
            clientSocket.send(response.encode())

def process_command(command, data, redis_instance) -> str:
    """ Processes the command and returns a response for the client"""
    if command == "SET":
        key, value = data[1], data[2]
        return redis_instance.set(key, value)
    elif command == "GET":
        key = data[1]
        return redis_instance.get(key) 
    elif command == "DEL":
        key = data[1]
        return str(redis_instance.delete(key))
    elif command == "EXPIRE":
        key, time = data[1], data[2]
        return redis_instance.expiration(key, time)
    else:
        return "Invalid command"
            
if __name__ == "__main__":
    try:
        start_server()
    except KeyboardInterrupt:
        print("Server shut down")