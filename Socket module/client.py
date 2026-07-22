import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(("192.168.23.130", 8080))

data = s.recv(1024).decode()
print("Server: ", data)

msg = input("You: ")
s.sendall(msg.encode())

sec_data = s.recv(1024).decode()
print("Server: ", sec_data)

s.close()