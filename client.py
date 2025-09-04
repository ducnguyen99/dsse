import socket
from Utils.TSet import TSet, cal_size, genStag
from Utils.XSet import XSet
from Utils.AUHME import AUHME

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

# tset = TSet()

# tset.setup()
# tset.update("add", "kw1", "f1")
# print(tset.search('kw1'))


xset_dict = {"kw1||f1": 1, "kw1||f2": 1, "kw1||f3": 0,
             "kw2||f1": 1, "kw2||f2": 1, "kw2||f3": 1,
             "kw3||f1": 1, "kw3||f2": 0, "kw3||f3": 1,}

xset = XSet()
xset.setup()
auhme = AUHME()
auhme.setup()
cnt = 1
local_addr = []
params = (cnt, local_addr)

for k, v in xset_dict.items():
  (utok, params) = auhme.gen_upd("add", k, v, params)
  xset.update(utok, auhme)

key_dict = [{"kw2||f1": 1, "kw3||f1": 1}, {"kw2||f2": 1, "kw3||f2": 1}]
dk = []
for i in key_dict:
  dk.append(auhme.key_gen(i, params))


res = xset.search(dk, auhme)
print(res)
