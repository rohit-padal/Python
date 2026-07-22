import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("8.8.8.8", 443))

print("Connected!")
print("My address: ",s.getsockname())
print("Server: ",s.getpeername())

s.close()