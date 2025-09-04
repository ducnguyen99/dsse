import socket

HOST = '0.0.0.0'  # Listen on all interfaces
PORT = 8000       # Listening port

# Create a TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)

print(f"Server listening on {HOST}:{PORT}")

while True:
    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")
    data = conn.recv(1024).decode()
    print(f"Received: {data}")
    conn.sendall(b"Message received!")
    conn.close()