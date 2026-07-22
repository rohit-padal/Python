import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(("0.0.0.0",8080))
# print("Bound successfully!")
# print(s.getsockname())

s.listen(5)
print("server is listening...")

client_socket, client_address = s.accept()
print("Client connected!")
print("client_address: ", client_address)
client_socket.close()

s.close()