import socket
from Utils.TSet import TSet, cal_size, genStag

# HOST = '127.0.0.1'  # Change this to server's IP if running remotely
# PORT = 8000

# # Create a TCP socket
# client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client_socket.connect((HOST, PORT))

# # Send message
# message = input()
# client_socket.sendall(message.encode())

# # Receive response
# response = client_socket.recv(1024).decode()
# print(f"Server replied: {response}")

# client_socket.close()

tset = TSet()

tset.setup()
tset.update("add", "kw1", "f1")